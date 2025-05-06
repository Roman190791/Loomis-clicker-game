# Loomis-clicker-game
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loomis Clicker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #111, #222);
      color: #fff;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    .container {
      margin-top: 60px;
    }
    .counter {
      font-size: 2em;
      margin: 20px 0;
    }
    .click-btn {
      font-size: 20px;
      padding: 15px 30px;
      border: none;
      border-radius: 10px;
      background: #00c853;
      color: white;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .click-btn:hover {
      background: #00e676;
    }
    .shop {
      margin-top: 40px;
    }
    .upgrade {
      margin: 10px 0;
    }
    .upgrade button {
      padding: 10px;
      background: #0091ea;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .upgrade button:disabled {
      background: #555;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Loomis Clicker</h1>
    <p class="counter">Монет: <span id="coins">0</span></p>
    <button class="click-btn" onclick="clickCoin()">Зібрати монету</button>

    <div class="shop">
      <h2>Покращення</h2>
      <div class="upgrade">
        <span>Автоклік (1 монета/сек) - 100 монет</span>
        <button onclick="buyAutoClick()" id="autoclick-btn">Купити</button>
      </div>
    </div>
  </div>

  <script>
    let coins = 0;
    let autoClickers = 0;
    let autoClickEnabled = false;

    // Завантаження з localStorage
    window.onload = () => {
      coins = parseInt(localStorage.getItem("coins")) || 0;
      autoClickers = parseInt(localStorage.getItem("autoClickers")) || 0;
      updateDisplay();
      if (autoClickers > 0) enableAutoClick();
    }

    function updateDisplay() {
      document.getElementById('coins').innerText = coins;
      localStorage.setItem("coins", coins);
    }

    function clickCoin() {
      coins++;
      updateDisplay();
    }

    function buyAutoClick() {
      if (coins >= 100 && !autoClickEnabled) {
        coins -= 100;
        autoClickers++;
        localStorage.setItem("autoClickers", autoClickers);
        enableAutoClick();
        document.getElementById('autoclick-btn').disabled = true;
      }
      updateDisplay();
    }

    function enableAutoClick() {
      autoClickEnabled = true;
      setInterval(() => {
        coins++;
        updateDisplay();
      }, 1000);
    }

    // Telegram або Trust Wallet інтеграція (замість MetaMask)
    function openWalletLink() {
      // Trust Wallet deep link або Telegram Wallet link
      const trustLink = "https://link.trustwallet.com/open_url?coin_id=60&url=https://loomis.click/pay";
      const telegramLink = "https://t.me/wallet/start?startapp=loomisclicker";

      // Відкриваємо у новій вкладці
      window.open(telegramLink, '_blank');
    }
  </script>
  <button onclick="openWalletLink()" style="margin-top: 30px; padding: 10px 20px; font-size: 16px;">
    Відкрити гаманець (Telegram або Trust)
  </button>
</body>
</html>
vercel.json
