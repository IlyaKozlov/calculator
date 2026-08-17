Предусловия:
Base URL: http://localhost:1743
1. Post/calculations
 * Параметры запроса
{
"firstNumber": "number"
"secondNumber": "number"
"operation": "string"
}
 * Параметры ответа
{
"result": "number"
}
 * 
2. Get/
 * Параметры ответа
{
"status": "ok"
}

Предусловие:
Использовать в поле operation параметры: "+","-","*","/"
1. Отправка запроса с валидными данными
Отправить запрос Post/calculations
Параметры запроса
{
"firstNumber": "1"
"secondNumber": "1"
"operation": "+"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "2"
}

Предусловие:
operation = "+" или "*"
для +: 5 + 4 = 4 + 5 = 9
для *: 5 * 4 = 4 * 5 = 20
2. Проверка перестановки операндов
Отправить запрос Post/calculations
Пример запроса "+"
{
"firstNumber": "5"
"secondNumber": "4"
"operation": "+"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "9"
}

Пример запроса "*"
{
"firstNumber": "5"
"secondNumber": "4"
"operation": "*"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "20"
}


3. Предусловие:
Post/calculations
Проверка операций с отрицательными числами
 1) сложение отрицательных чисел
Параметры запроса
{
"firstNumber": "-1"
"secondNumber": "-1"
"operation": "+"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "-2"
}
 2) вычитание отрицательных чисел
Параметры запроса
{
"firstNumber": "-1"
"secondNumber": "-1"
"operation": "-"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "0"
}

4. Проверка деления нуля на число
Отправить запрос Post/calculations

Параметры запроса
{
"firstNumber": "0"
"secondNumber": "5"
"operation": "/"
}
Ожидаемый результат:
Код 200 ОК
Параметры ответа
{
"result": "0"
}

5. Проверка деления на ноль
Отправить запрос Post/calculations
Параметры запроса
{
"firstNumber": "5"
"secondNumber": "0"
"operation": "/"
}
Ожидаемый результат:
Код 400 Error: Bad Request
Параметры ответа
{
  "detail": "Second number cannot be zero"
}
6. Отправить запрос с невалидной операцией
Отправить запрос Post/calculations
Параметры запроса
{
"firstNumber": "2"
"secondNumber": "1"
"operation": "%"
}
Ожидаемый результат:
Код 400 Error: Bad Request
Параметры ответа
{
  "detail": "Invalid operation %"
}

7. Проверка обязательных полей
Отправить запрос Post/calculations
Параметры запроса
{
"secondNumber": "1"
"operation": "-"
}
Ожидаемый результат:
Код 400 Error: Bad Request
Параметры ответа
{
  "detail": "Invalid parameter"
}

8. Отправка невалидного запроса
Отправить запрос Post/calculations
Параметры запроса
{
"firstNumber": " "
"secondNumber": " "
"operation": " "
}
Ожидаемый результат:
Код 400 Error: Bad Request
Параметры ответа
{
  "detail": "Invalid Request"
}

9. Проверка Get запроса
Отправить запрос Get/
Ожидаемый результат:
Код 200 ОК
{
  "status": "ok"
}