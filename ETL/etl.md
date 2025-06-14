# ETL 
![pipleETl](/image/pipeETL.png)
Автоматизированный процесс поставки новых данных в хранилища называется ETL (от англ. Extract, Transform, Load — «извлечение, трансформация, загрузка»).  

---

Работа над проектированием ETL-процесса начинается с анализа источников данных.  
**Источники бывают разные — OLTP, OLAP, API, файловые хранилища, и подключение к каждому происходит по-разному:** 
![sources](/image/sources.png) 
- К OLTP и OLAP базам можно подключиться напрямую с помощью Python или сформировать SQL-запросы на сбор данных.  
- Работа с API осуществляется с помощью запросов с авторизацией, для которых удобно использовать методы `requests.post()` и `requests.get()`. Запрашивать данные через API можно синхронно (запрашиваем и получаем результат в рамках одного процесса) и асинхронно (один процесс для запроса данных, второй — для получения).  
- Выгрузить данные из хранилища можно по ссылке или по прямому пути, который есть у каждого файла.  

---

## Слои  
![layer](/image/layer.png)

#### 🔹 RAW — **Raw** (Сырые данные)
🚀 **Описание:**  
Это первый слой, куда загружаются данные напрямую из всех систем-источников.  
Данные поступают «как есть», без очистки и преобразований.  
✅ Используется для сохранности полного набора событий на всякий случай.

#### 🔹 ODS — **Operational Data Store** (Операционное хранилище)
🧹 **Описание:**  
На этом слое данные очищаются, нормализуются и концентрируют на главнейших атрибутах.  
Можно заполнить пропуски, перевести поля к единообразию и убрать ошибки.  
✅ Используется для повышения качества и согласованности информации.

#### 🔹 DDS — **Data Delivery Store** (Детализированное хранилище)
🏛 **Описание:**  
Это главная среда с точными правилами связи, ключами и нормализацией.  
Не концентрат, а всё на уровне событий, с полными связями.  
✅ Используется для точной аналитики и прогнозирования на всех слоях бизнеса.

#### 🔹 CDM — **Comprehensive Data Model** (Шина данных / концентрат)
🌟 **Описание:**  
Это концентрат всех деталей из DDS, переведённых в структуры, которые проще использовать аналитиками.  
Не такой подробный, концентрирует главные меры и свойства.  
✅ Используется для создания аналитических витрин, звёздных и снежинковых схем.

#### 🔹 REP — **Reporting** (Отчетный слой)
📊 **Описание:**  
Финальный слой с полностью агрегированными и легкодоступными данными.  
Не нужно делать JOIN — всё готово для применения.  
✅ Используется для создания отчётов, дешбордов и других аналитических приложений.  

---

### 📝 Логирование

- ⏱ Время **начала работы пайплайна**
- 🔗 **Подключение к источнику**
- ⏱ Время **начала загрузки данных** в хранилище
- 🏪 **Уровень хранилища**, в который загружается информация
- 🔹 **Название задачи и номер шага процесса** — для легкости поиска ошибки, особенно когда задач много
- ⏳ Как долго **выполняется шаг**
- ✅ **Успешный либо неуспешный статус** такого шага
- ⚡ Последнее **сообщение либо описание ошибки**  

---

### Маппинг  
![mapping](/image/mapping.png)

## 📝 Мапинг данных (data mapping)

#### 🔹 Что это?

**Мапинг данных** — это процесс установления соответствия (соединения) полей из **источника** с полями **приёмника** (например, из одной системы в базу данных, из старой модели данных — в новую).

#### 🔹 Задача мапинга

- Соединить структуры данных из **разных систем**
- Соотнести названия и свойства полей
- Обеспечить точное и полное перенесение информации

#### 🔹 Зачем нужно?

✅ Когда системы имеют разные названия колонок, разные типы данных, структуры.  
✅ Когда нужно перейти с одной модели на другую, сохранив логику и качество информации.

#### 🔹 Что учитывает мапинг?

- **Наименование полей**
- **Тип данных**
- **Формат**
- **Необходимость преобразования** (например, из `integer` в `string`)
- **Бизнес-правила**, которые нужно выполнить при преобразовании (например, слияние нескольких полей, расчет новых)

#### 🔹 Результат мапинга:

✅ Четкое описание правила переноса из одной системы в другую.  
✅ Используется специалистами (ETL-разработчиками, аналитиками) для написания алгоритмов преобразования.

---

🚀 Всё это позволяет эффективно и правильно загружать данные из различных систем, сохранив структуру и качество информации.

