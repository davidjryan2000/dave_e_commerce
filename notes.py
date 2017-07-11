
cart  views.py 
def select_order(request, id):
    types = {"type1":50,"type2":60,"type3":279,"type4":325,"type5":379,"type6":850,"type7":450,"type8":1850,"type9":950}
    order = request.POST['types']
    print(order)
    cartItem = CartItem.objects.get(id=id)
    cartItem.order = types.values
    cartItem.save()
    print(cartItem)
    return redirect(reverse('cart'))

cart urls.py
url(r'^adjust/(?P<id>\d+)', select_order, name='select_order')








