# Система тестирования студентов

Система для проведения тестирования студентов с различными типами вопросов.

## Функциональность

- Три типа вопросов:
  - Открытые вопросы
  - Вопросы с выбором ответа
  - Вопросы на соответствие
- Ограничение по времени (30 минут)
- Адаптивный дизайн
- Подробные результаты с визуализацией

## Установка

1. Убедитесь, что у вас установлен Node.js (версия 14 или выше)
2. Клонируйте репозиторий
3. Установите зависимости:
```bash
npm install
```

## Запуск

1. Запустите сервер:
```bash
npm start
```
2. Откройте в браузере http://localhost:3000

## Структура проекта

- `server.js` - основной файл сервера
- `public/` - статические файлы
  - `index.html` - главная страница
  - `test.html` - страница теста
  - `results.html` - страница результатов
  - `styles.css` - стили
  - `app.js` - JavaScript для главной страницы
  - `test.js` - JavaScript для страницы теста
  - `results.js` - JavaScript для страницы результатов 