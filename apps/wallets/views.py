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
    wallet_data = WalletChecker(address).get_wallet_data()
    context = {
        'address': address,
        'wallet_data': wallet_data,
    }
    return render(request, 'wallets/wallet_detail.html', context)
