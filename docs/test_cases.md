# Тест-кейсы API онлайн-калькулятора

## Предусловия

**Base URL:** `http://localhost:1743`

### POST /calculations

**Параметры запроса:**

```json
{
  "firstNumber": "number",
  "secondNumber": "number",
  "operation": "string"
}
```

**Параметры ответа:**

```json
{
  "result": "number"
}
```

### GET /

**Параметры ответа:**

```json
{
  "status": "ok"
}
```

---

## 1. Отправка запроса с валидными данными

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": 1,
  "secondNumber": 1,
  "operation": "+"
}
```

### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "result": 2
}
```

---

## 2. Проверка перестановки операндов

**Предусловие:** операция принимает значение `+` или `*`.

Проверяемые равенства:

- `5 + 4 = 4 + 5 = 9`
- `5 * 4 = 4 * 5 = 20`

**Endpoint:** `POST /calculations`

### 2.1. Проверка перестановки операндов для сложения

#### Первый запрос

```json
{
  "firstNumber": 5,
  "secondNumber": 4,
  "operation": "+"
}
```

**Ожидаемый результат:**

**HTTP 200 OK**

```json
{
  "result": 9
}
```

#### Второй запрос

```json
{
  "firstNumber": 4,
  "secondNumber": 5,
  "operation": "+"
}
```

**Ожидаемый результат:**

**HTTP 200 OK**

```json
{
  "result": 9
}
```

Результаты первого и второго запросов должны совпадать.

### 2.2. Проверка перестановки операндов для умножения

#### Первый запрос

```json
{
  "firstNumber": 5,
  "secondNumber": 4,
  "operation": "*"
}
```

**Ожидаемый результат:**

**HTTP 200 OK**

```json
{
  "result": 20
}
```

#### Второй запрос

```json
{
  "firstNumber": 4,
  "secondNumber": 5,
  "operation": "*"
}
```

**Ожидаемый результат:**

**HTTP 200 OK**

```json
{
  "result": 20
}
```

Результаты первого и второго запросов должны совпадать.

---

## 3. Проверка операций с отрицательными числами

**Endpoint:** `POST /calculations`

### 3.1. Сложение отрицательных чисел

#### Параметры запроса

```json
{
  "firstNumber": -1,
  "secondNumber": -1,
  "operation": "+"
}
```

#### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "result": -2
}
```

### 3.2. Вычитание отрицательных чисел

#### Параметры запроса

```json
{
  "firstNumber": -1,
  "secondNumber": -1,
  "operation": "-"
}
```

#### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "result": 0
}
```

---

## 4. Проверка деления нуля на число

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": 0,
  "secondNumber": 5,
  "operation": "/"
}
```

### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "result": 0
}
```

---
## 4. Проверка округления дробного результата

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": 10,
  "secondNumber": 3,
  "operation": "/"
}
```

### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "result": 3.33
}
```


## 6. Проверка деления на ноль

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": 5,
  "secondNumber": 0,
  "operation": "/"
}
```

### Ожидаемый результат

**HTTP 400 Bad Request**

```json
{
  "detail": "Second number cannot be zero"
}
```

---

## 7. Отправка запроса с невалидной операцией

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": 2,
  "secondNumber": 1,
  "operation": "%"
}
```

### Ожидаемый результат

**HTTP 400 Bad Request**

```json
{
  "detail": "Invalid operation %"
}
```

---

## 8. Проверка обязательного поля

**Endpoint:** `POST /calculations`

В запросе отсутствует обязательное поле `firstNumber`.

### Параметры запроса

```json
{
  "secondNumber": 1,
  "operation": "-"
}
```

### Ожидаемый результат

**HTTP 400 Bad Request**

```json
{
  "detail": "Invalid parameter"
}
```

---

## 9. Отправка невалидного запроса

**Endpoint:** `POST /calculations`

### Параметры запроса

```json
{
  "firstNumber": " ",
  "secondNumber": " ",
  "operation": " "
}
```

### Ожидаемый результат

**HTTP 400 Bad Request**

```json
{
  "detail": "Invalid request"
}
```

---

## 10. Проверка GET-запроса

**Endpoint:** `GET /`

### Ожидаемый результат

**HTTP 200 OK**

```json
{
  "status": "ok"
}
```