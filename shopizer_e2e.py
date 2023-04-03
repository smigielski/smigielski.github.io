from requests_html import HTMLSession

session = HTMLSession()

# Browse to the product page and add the product to cart
product_url = 'http://localhost:8080/shopizer/shop/product/4/flower-printed-dress'
cart_url = ''
r = session.get(product_url)
r.html.render()
cart_button = r.html.find('#add-to-cart-button', first=True)
if cart_button is not None:
    r = cart_button.click()
    r.html.render()
    cart_url = r.url

# Browse to the cart page and proceed to checkout
if cart_url != '':
    r = session.get(cart_url)
    r.html.render()
    checkout_button = r.html.find('#checkoutButton', first=True)
    if checkout_button is not None:
        r = checkout_button.click()
        r.html.render()
        form = r.html.find('#billingForm', first=True)
        if form is not None:
            form.find('#customer.firstName', first=True).fill('John')
            form.find('#customer.lastName', first=True).fill('Doe')
            form.find('#billingAddress.address', first=True).fill('123 Main St')
            form.find('#billingAddress.city', first=True).fill('Anytown')
            form.find('#billingAddress.stateProvince', first=True).fill('CA')
            form.find('#billingAddress.postalCode', first=True).fill('12345')
            form.find('#customer.phoneNumber', first=True).fill('555-1234')
            form.find('#customer.emailAddress', first=True).fill('john.doe@example.com')
            r = form.find('button[type="submit"]', first=True).click()
            r.html.render()
            print('Checkout completed successfully!')
        else:
            print('Could not find billing form.')
    else:
        print('Could not find checkout button.')
else:
    print('Could not find cart URL.')

