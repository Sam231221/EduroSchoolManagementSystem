from .forms import LogInForm, SignUpForm


def forms(request):
    return {'signupform':SignUpForm(),
            'loginform':LogInForm()
            }
