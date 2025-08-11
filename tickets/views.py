from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.conf import settings

from .forms import TicketForm
from .models import Ticket

import os
from pathlib import Path
import joblib

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)


def get_model():
    ml_path = Path(__file__).parent / 'ml' / 'model.pkl'
    model = joblib.load(ml_path)
    return model


def get_sentiment_score(text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    return sentiment['compound']


class SubmitTicketView(FormView):
    template_name = "tickets/submit.html"
    form_class = TicketForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_css_cdn'] = settings.BOOTSTRAP_CSS_CDN
        return context

    def form_valid(self, form):
        model = get_model()
        description = form.cleaned_data['description']
        urgency = form.cleaned_data['urgency']

        # Predict category from description
        predicted_category = model.predict([description])[0]

        # Compute sentiment compound score
        sentiment_compound = get_sentiment_score(description)

        # priority_score = sentiment * urgency converted to float
        priority_score = sentiment_compound * float(urgency)

        # Save ticket
        Ticket.objects.create(
            customer_name=form.cleaned_data['customer_name'],
            email=form.cleaned_data['email'],
            description=description,
            urgency=urgency,
            category=predicted_category,
            priority_score=priority_score
        )
        return super().form_valid(form)


class DashboardView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = "tickets/dashboard.html"

    def get_queryset(self):
        return Ticket.objects.all().order_by('-priority_score')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_css_cdn'] = settings.BOOTSTRAP_CSS_CDN
        # Prepare sentiment scores for each ticket for display
        for ticket in context['tickets']:
            ticket.sentiment = get_sentiment_score(ticket.description)
        return context

    def post(self, request, *args, **kwargs):
        mapping = {
            'Billing': 'Agent A',
            'Technical': 'Agent B',
            'General': 'Agent C',
            'Complaint': 'Agent D',
        }
        tickets_to_assign = Ticket.objects.filter(assigned_agent__isnull=True)
        for ticket in tickets_to_assign:
            agent = mapping.get(ticket.category)
            if agent:
                ticket.assigned_agent = agent
                ticket.save()
        return redirect('dashboard')
