function $(id) {
  return document.getElementById(id);
}

function setResult(id, text) {
  var el = $(id);
  if (el) el.textContent = text;
}

function toNumber(value) {
  var n = Number(value);
  return Number.isFinite(n) ? n : 0;
}

var page = document.body.dataset.page;

if (page === 'atm') {
  var balances = { k: 50000, s: 100000, i: 60000 };
  var pins = { k: '1234', s: '5678', i: '9123' };
  var names = { k: 'Ken Keneki', s: 'Sasuke Uchiha', i: 'Itachi Uchiha' };

  $('atmRun').addEventListener('click', function () {
    var card = $('atmCard').value;
    var pin = $('atmPin').value.trim();
    var action = $('atmAction').value;
    var amount = toNumber($('atmAmount').value);
    var balance = balances[card];

    if (pin !== pins[card]) {
      setResult('atmResult', 'Incorrect pin. Access blocked in this simulation after two tries.');
      return;
    }

    if (action === 'balance') {
      setResult('atmResult', names[card] + ', your current balance is Rs ' + balance + '.');
      return;
    }

    if (amount <= 0) {
      setResult('atmResult', 'Please enter a valid withdrawal amount.');
      return;
    }

    if (amount > balance) {
      setResult('atmResult', 'Insufficient funds. Available balance is Rs ' + balance + '.');
      return;
    }

    setResult(
      'atmResult',
      'Withdrawal successful for ' + names[card] + '.\nDispensed: Rs ' + amount + '\nRemaining balance: Rs ' + (balance - amount) + '.'
    );
  });
}

if (page === 'billing') {
  var rates = {
    body_soap: 10,
    hair_cream: 25,
    body_spray: 50,
    hair_spray: 50,
    sugar: 100,
    tea: 15,
    coffee: 50,
    rice: 150,
    wheat: 160,
    pepsi: 30,
    sprite: 35,
    coke: 30,
    mojitos: 25,
    thumbs_up: 35
  };

  $('billRun').addEventListener('click', function () {
    var total = 0;
    Object.keys(rates).forEach(function (key) {
      var qty = toNumber($(key).value);
      total += qty * rates[key];
    });
    setResult('billResult', 'Estimated total: Rs ' + total + '\nThis mirrors the pricing flow from billing.c.');
  });
}

if (page === 'casino') {
  $('casinoPlay').addEventListener('click', function () {
    var deposit = toNumber($('casinoDeposit').value);
    var bet = toNumber($('casinoBet').value);
    var guess = toNumber($('casinoGuess').value);
    var lucky = Math.floor(Math.random() * 10) + 1;

    if (deposit <= 0 || bet <= 0) {
      setResult('casinoResult', 'Deposit and bet must be positive values.');
      return;
    }
    if (bet > deposit) {
      setResult('casinoResult', 'Bet cannot exceed current deposit.');
      return;
    }
    if (guess < 1 || guess > 10) {
      setResult('casinoResult', 'Pick a number between 1 and 10.');
      return;
    }

    if (guess === lucky) {
      setResult('casinoResult', 'You guessed ' + lucky + '. Jackpot. You win Rs ' + (bet * 10) + '.');
    } else {
      setResult(
        'casinoResult',
        'You guessed ' + guess + ', lucky number was ' + lucky + '.\nLoss: Rs ' + bet + '\nBalance left: Rs ' + (deposit - bet) + '.'
      );
    }
  });
}

if (page === 'guess') {
  var secret = 5;
  var tries = 0;
  $('guessRun').addEventListener('click', function () {
    var value = toNumber($('guessInput').value);
    tries += 1;
    if (value === secret) {
      setResult('guessResult', 'You Won in ' + tries + ' attempt(s). Secret number was 5.');
      tries = 0;
    } else if (tries >= 3) {
      setResult('guessResult', 'You Lost. You used all 3 attempts. Secret number was 5.');
      tries = 0;
    } else {
      setResult('guessResult', 'Not correct. Attempts left: ' + (3 - tries) + '.');
    }
  });
}

if (page === 'library') {
  $('libraryRun').addEventListener('click', function () {
    var category = $('libCategory').value;
    var book = $('libBook').value;
    setResult('libraryResult', 'Category: ' + category + '\nSelected: ' + book + '\nStatus: 2 copies left (demo flow inspired by lib_manage.c).');
  });
}

if (page === 'periodic') {
  var data = {
    1: {
      name: 'Hydrogen',
      symbol: 'H',
      config: '1s^1',
      discovered: 'Henry Cavendish',
      charge: '+1'
    },
    2: {
      name: 'Helium',
      symbol: 'He',
      config: '1s^2',
      discovered: 'Pierre Janssen',
      charge: '0'
    },
    6: {
      name: 'Carbon',
      symbol: 'C',
      config: '[He] 2s^2 2p^2',
      discovered: 'Ancient',
      charge: '+4/-4'
    }
  };

  $('periodicRun').addEventListener('click', function () {
    var z = toNumber($('atomicNumber').value);
    var el = data[z];
    if (!el) {
      setResult('periodicResult', 'Element not in this mini demo. Try 1, 2, or 6.');
      return;
    }
    setResult(
      'periodicResult',
      'Name: ' + el.name + '\nSymbol: ' + el.symbol + '\nAtomic Number: ' + z + '\nElectronic Configuration: ' + el.config + '\nDiscovered By: ' + el.discovered + '\nCharge: ' + el.charge
    );
  });
}

if (page === 'phone') {
  var contacts = [];
  $('phoneAdd').addEventListener('click', function () {
    var contact = {
      name: $('pbName').value.trim(),
      age: toNumber($('pbAge').value),
      phone: $('pbPhone').value.trim(),
      dob: $('pbDob').value.trim(),
      address: $('pbAddress').value.trim()
    };

    if (!contact.name || !contact.phone) {
      setResult('phoneResult', 'Name and phone number are required.');
      return;
    }

    contacts.push(contact);
    var lines = contacts.map(function (c, i) {
      return (
        (i + 1) + '. ' + c.name + ' | Age ' + c.age + ' | ' + c.phone + ' | DOB ' + c.dob + ' | ' + c.address
      );
    });
    setResult('phoneResult', 'Saved contacts:\n' + lines.join('\n'));
  });
}

if (page === 'quiz') {
  var score = 0;
  $('quizRun').addEventListener('click', function () {
    score = 0;
    var answers = {
      q1: '2',
      q2: '4',
      q3: '2',
      q4: '1',
      q5: '3'
    };

    Object.keys(answers).forEach(function (q) {
      var selected = document.querySelector('input[name="' + q + '"]:checked');
      if (selected && selected.value === answers[q]) score += 5;
    });

    setResult('quizResult', 'Your total score: ' + score + ' / 25');
  });
}
