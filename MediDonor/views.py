from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from MediDonor.forms import DonateForm, NomineeForm, PostingForm

from MediDonor.models import post, Organ, nominee
from MediUser.models import MediUser, Donation


def homepage(request):
    return render(request, 'MediUser/base.html')


class DonateView(SuccessMessageMixin, CreateView):
    model = Organ
    form_class = DonateForm
    success_url = reverse_lazy('base')
    template_name = 'MediDonor/donate.html'
    success_message = "Your data saved successfully"

    def post(self, request, *args, **kwargs):
        donor = MediUser.objects.get(username=request.user.username)

        blood_group = request.POST["blood_group"]
        organ_type = request.POST["organ_type"]
        organ_age = request.POST["organ_age"]
        s = Organ(user_id=donor, blood_group=blood_group, organ_type=organ_type, organ_age=organ_age)
        s.save()

        donate = Organ.objects.filter(user_id_id=donor.id).all()

        for do in donate:
            d = Donation(user_id_id=donor.id, organ_id_id=do.id)
            d.save()

        return render(request, 'MediUser/base.html')


class DonationView(ListView):
    queryset = Donation.objects.all().order_by('-id')
    template_name = 'MediDonor/donation.html'
    context_object_name = 'pro'


class DonateUpdateView(UpdateView):
    template_name = 'MediUser/donate.html'
    success_url = reverse_lazy('profile')
    queryset = Organ.objects.all()
    model = Organ
    form_class = DonateForm


class DonateDeleteView(DeleteView):
    success_url = reverse_lazy('profile')
    queryset = Organ.objects.all()


class NomineeView(CreateView):
    template_name = 'MediDonor/nominee.html'
    queryset = nominee.objects.all()
    form_class = NomineeForm
    success_message = "Your data saved successfully"

    def post(self, request, *args, **kwargs):
        donor = MediUser.objects.get(username=request.user.username)
        nominee_name = request.POST['nominee_name']
        nominee_email = request.POST['nominee_email']
        nominee_mobile = request.POST['nominee_mobile']
        relation = request.POST['relation']
        s = nominee(donor_id_id=donor.id, nominee_name=nominee_name, nominee_email=nominee_email,
                    nominee_mobile=nominee_mobile, relation=relation)
        s.save()
        return render(request, 'MediUser/base.html')


class NomineeUpdateView(UpdateView):
    template_name = 'MediDonor/nominee.html'
    form_class = NomineeForm
    success_url = reverse_lazy('profile')
    model = nominee


class NomineeDeleteView(DeleteView):
    success_url = reverse_lazy('profile')
    queryset = nominee.objects.all()


class PostView(ListView):
    queryset = post.objects.all().order_by('-id')
    template_name = 'MediDonor/post.html'
    context_object_name = 'pro'

    # def get_queryset(self):
    #    return self.queryset.aggregrate(duration=F('end_date') - F('start_date'))


class PostingView(CreateView):
    model = post
    queryset = post.objects.all()
    form_class = PostingForm
    template_name = 'MediDonor/posting.html'
    success_url = reverse_lazy('post')

    def post(self, request, *args, **kwargs):
        u = MediUser.objects.get(username=request.user.username)
        title = request.POST['title']
        location = request.POST['location']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        s = post(user_id_id=u.id, title=title, location=location,
                 description=description, start_date=start_date, end_date=end_date)
        s.save()
        return redirect('post')


class PostUpdateView(UpdateView):
    template_name = 'MediDonor/posting.html'
    success_url = reverse_lazy('profile')
    queryset = post.objects.all()
    form_class = PostingForm


class PostDeleteView(DeleteView):
    success_url = reverse_lazy('profile')
    queryset = post.objects.all()
