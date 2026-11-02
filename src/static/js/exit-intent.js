document.addEventListener('DOMContentLoaded', () => {
  const popup = document.createElement('div');
  popup.id = 'exit-intent-popup';
  popup.style.cssText = 'position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); display:none; justify-content:center; align-items:center; z-index:9999;';
  popup.innerHTML = `
    <div style="background:white; padding:2rem; border-radius:8px; text-align:center; max-width:400px;">
      <h2>Wait! Don't leave yet.</h2>
      <p>Get 15% off our Professional Plan if you sign up today.</p>
      <button id="close-popup" style="padding:10px 20px; cursor:pointer;">Claim Discount</button>
    </div>
  `;
  document.body.appendChild(popup);

  document.addEventListener('mouseleave', (e) => {
    if (e.clientY < 0) {
      popup.style.display = 'flex';
    }
  });

  document.getElementById('close-popup').addEventListener('click', () => {
    popup.style.display = 'none';
    window.location.href = '/checkout?discount=15OFF';
  });
});