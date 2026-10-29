const displayValue = document.querySelector('#display-value');
const previousExpression = document.querySelector('#previous-expression');
const errorMessage = document.querySelector('#error-message');
const operatorButtons = [...document.querySelectorAll('[data-operation]')];
const historyList = document.querySelector('#history-list');
const emptyHistory = document.querySelector('#empty-history');
const historyOperationFilter = document.querySelector('#history-operation-filter');

let currentValue = '';
let firstValue = null;
let operation = null;
let waitingForSecondValue = false;
let lastExpression = '';
let historyItems = [];

function getSessionId() {
  let sessionId = sessionStorage.getItem('calculator-session-id');
  if (!sessionId) {
    sessionId = crypto.randomUUID();
    sessionStorage.setItem('calculator-session-id', sessionId);
  }
  return sessionId;
}

const sessionId = getSessionId();

function render() {
  displayValue.textContent = currentValue || '0';
  previousExpression.textContent = firstValue !== null && operation
    ? `${formatNumber(firstValue)} ${operation === '*' ? '×' : operation}`
    : lastExpression;
  operatorButtons.forEach((button) => button.classList.toggle('is-selected', button.dataset.operation === operation));
}

function formatNumber(value) {
  return Number.isInteger(value) ? String(value) : String(Number(value.toFixed(10)));
}

function showError(message) {
  errorMessage.textContent = message;
}


function renderHistory() {
  historyList.replaceChildren();
  emptyHistory.hidden = historyItems.length > 0;
  historyItems.forEach(({ expression, result }) => {
    const item = document.createElement('li');
    const expressionElement = document.createElement('span');
    const resultElement = document.createElement('strong');
    item.className = 'history__item';
    expressionElement.textContent = expression;
    resultElement.textContent = result;
    item.append(expressionElement, resultElement);
    historyList.appendChild(item);
  });
}

function getHistoryResult(firstNumber, operation, secondNumber) {
  if (operation === '+') return firstNumber + secondNumber;
  if (operation === '-') return firstNumber - secondNumber;
  if (operation === '*') return firstNumber * secondNumber;
  if (operation === '/' && secondNumber !== 0) return firstNumber / secondNumber;
  return null;
}

async function loadHistory() {
  try {
    const params = new URLSearchParams({ session_id: sessionId });
    if (historyOperationFilter.value) params.set('operation', historyOperationFilter.value);
    const response = await fetch(`/history?${params}`);
    if (!response.ok) throw new Error('Не удалось загрузить историю');
    const savedItems = await response.json();

    historyItems = savedItems
      .reverse()
      .map(({ first_number, operation, second_number }) => {
        const result = getHistoryResult(first_number, operation, second_number);
        if (result === null) return null;
        return {
          operation,
          expression: `${formatNumber(first_number)} ${operation === '*' ? '×' : operation} ${formatNumber(second_number)} =`,
          result: formatNumber(result),
        };
      })
      .filter(Boolean);
    renderHistory();
  } catch (error) {
    showError(error.message);
  }
}

function inputNumber(number) {
  showError('');
  if (waitingForSecondValue) {
    currentValue = '';
    waitingForSecondValue = false;
  }
  if (currentValue === '0') currentValue = '';
  if (currentValue.length < 16) currentValue += number;
  render();
}

function inputDecimal() {
  showError('');
  if (waitingForSecondValue) {
    currentValue = '0';
    waitingForSecondValue = false;
  }
  if (!currentValue) currentValue = '0';
  if (!currentValue.includes('.')) currentValue += '.';
  render();
}

function chooseOperation(nextOperation) {
  showError('');
  if (!currentValue && firstValue === null) return;
  if (firstValue !== null && !waitingForSecondValue) calculate(false);
  firstValue = Number(currentValue);
  operation = nextOperation;
  waitingForSecondValue = true;
  render();
}

async function calculate(showResult = true) {
  if (firstValue === null || operation === null || waitingForSecondValue || !currentValue) return;
  const secondValue = Number(currentValue);
  try {
    const response = await fetch('/calculations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        firstNumber: firstValue,
        secondNumber: secondValue,
        operation,
        sessionId,
      }),
    });
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Не удалось выполнить вычисление');
    }
    const result = await response.json();
    lastExpression = `${formatNumber(firstValue)} ${operation === '*' ? '×' : operation} ${formatNumber(secondValue)} =`;
    currentValue = formatNumber(result);
    if (!historyOperationFilter.value || historyOperationFilter.value === operation) {
      historyItems.unshift({ operation, expression: lastExpression, result: currentValue });
      renderHistory();
    }
    firstValue = null;
    operation = null;
    waitingForSecondValue = false;
    render();
  } catch (error) {
    showError(error.message);
  }
}

function clearCalculator() {
  currentValue = '';
  firstValue = null;
  operation = null;
  lastExpression = '';
  waitingForSecondValue = false;
  showError('');
  render();
}

document.querySelectorAll('[data-number]').forEach((button) => button.addEventListener('click', () => inputNumber(button.dataset.number)));
document.querySelector('[data-action="decimal"]').addEventListener('click', inputDecimal);
document.querySelectorAll('[data-operation]').forEach((button) => button.addEventListener('click', () => chooseOperation(button.dataset.operation)));
document.querySelector('[data-action="equals"]').addEventListener('click', () => calculate());
document.querySelector('[data-action="clear"]').addEventListener('click', clearCalculator);
document.querySelector('[data-action="backspace"]').addEventListener('click', () => {
  if (!waitingForSecondValue) currentValue = currentValue.slice(0, -1);
  render();
});


historyOperationFilter.addEventListener('change', loadHistory);

document.querySelector('#clear-history').addEventListener('click', async () => {
  try {
    const response = await fetch(`/history?session_id=${encodeURIComponent(sessionId)}`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Не удалось очистить историю');
    historyItems = [];
    renderHistory();
  } catch (error) {
    showError(error.message);
  }
});

document.querySelectorAll('[data-view]').forEach((tab) => tab.addEventListener('click', () => {
  document.querySelectorAll('.view').forEach((view) => {
    view.hidden = view.id !== tab.dataset.view;
  });
  document.querySelectorAll('[data-view]').forEach((item) => item.classList.toggle('is-active', item === tab));
}));

document.addEventListener('keydown', (event) => {
  if (/^[0-9]$/.test(event.key)) inputNumber(event.key);
  else if (event.key === '.') inputDecimal();
  else if ('+-*/'.includes(event.key)) chooseOperation(event.key);
  else if (event.key === 'Enter' || event.key === '=') calculate();
  else if (event.key === 'Escape') clearCalculator();
  else if (event.key === 'Backspace') document.querySelector('[data-action="backspace"]').click();
});

render();
renderHistory();
loadHistory();
