from django.shortcuts import render, redirect

from apps.wallets.forms import WalletAddressForm
from apps.wallets.wallet_checker import WalletChecker


def index(request):
    if request.method == "POST":
        form = WalletAddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            return redirect("wallets:detail", address=address)
    else:
        form = WalletAddressForm()

    return render(request, 'wallets/index.html', {'form': form})


def wallet_detail(request, address):
    context = {
        'address': address,
        'wallet_data': WalletChecker().get_wallet_data(address)
    }
    return render(request, 'wallets/wallet_detail.html', context)
