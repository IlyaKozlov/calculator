Предусловие:
host port = 1743
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


1. Отправка запроа с валидными данными
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
2. Проверка деления на ноль
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
3. Отправить запрос с невалидной операцией
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
4. Проверка Get запроса
Отправить запрос Get/
Ожидаемый результат:
Код 200 ОК
{
  "status": "ok"
}