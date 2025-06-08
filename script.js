window.addEventListener('DOMContentLoaded', () => {
  const tg = window.Telegram.WebApp;
  tg.expand();

  const START_BALANCE = 50000n; // 50 000 LumisCoin глобальний запас
  let totalBalance = START_BALANCE;
  let playerBalance = 0n;

  const btnStart = document.getElementById('btn-start');
  const btnClick = document.getElementById('btn-click');
  const scoreEl = document.getElementById('score');

  btnStart.addEventListener('click', () => {
    btnClick.disabled = false;
    btnStart.disabled = true;
    updateScore();
  });

  btnClick.addEventListener('click', () => {
    if (totalBalance < 5n) {
      alert('Глобальний запас закінчився!');
      btnClick.disabled = true;
      return;
    }
    playerBalance += 5n;
    totalBalance -= 5n;
    updateScore();
  });

  function updateScore() {
    scoreEl.textContent = `LumisCoin: ${playerBalance.toString()}`;
  }
});
