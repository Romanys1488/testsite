from django import forms


ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

ITEM_SIZE_CHOICES = [(1, 'XS'), (2,'S'), (3, 'M'), (4, 'L'), (5, 'XL')]

class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(
                            choices = ITEM_QUANTITY_CHOICES,
                            coerce = int)



    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
