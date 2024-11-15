# **TB5 - Трекер задач сотрудников**
### **Описание задачи:**

Необходимо реализовать серверное приложение для работы с базой данных, представляющее собой трекер задач сотрудников. Приложение должно обеспечивать CRUD операции для сотрудников и задач, а также предоставлять два специальных эндпоинта для получения информации о загруженности сотрудников и важных задачах.
Трекер задач позволит компании эффективно управлять заданиями, назначенными сотрудникам, и обеспечивать прозрачность процессов выполнения задач. Это поможет в равномерном распределении нагрузки между сотрудниками и своевременном выполнении ключевых задач.
>#### **Специальные эндпоинты:**
>- Занятые сотрудники:
> 
> Запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач.
>- Важные задачи:
> 
> Запрашивает из БД задачи, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу.
> 
>  Реализует поиск по сотрудникам, которые могут взять такие задачи (менее загруженный сотрудник или сотрудник выполняющий родительску задачу, если ему назначено на 2 задачи больше чем у наименее загруженного).
> 
> Возвращает список объектов в формате: {Важная задача, Срок, [ФИО сотрудника]}.

### **Требования**
- Python
- Django
- DRF
- PostgreSQL
- Docker
