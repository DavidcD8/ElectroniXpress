const stripe = Stripe('pk_test_OkJAbpCYKOtDIINu3s3PqEwA');
const elements = stripe.elements();
const card = elements.create('card', {
  style: {
    base: {
      fontSize: '16px',
      color: '#32325d',
    },
  },
  hidePostalCode: true, // This line hides the postal code field
});

card.mount('#card-element');

const form = document.getElementById('payment-form');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const { token, error } = await stripe.createToken(card);

  if (error) {
    const errorElement = document.getElementById('card-errors');
    errorElement.textContent = error.message;
  } else {
    stripeTokenHandler(token);
  }
});

function stripeTokenHandler(token) {
  const form = document.getElementById('payment-form');
  const hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);
  form.submit();
}
