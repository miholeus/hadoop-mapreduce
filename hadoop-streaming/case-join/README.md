> Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя. Первый
> файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
> Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой
> системе.
>
> Mapper передает данные в reducer в виде key / value, где key - id пользователя, value
> состоит из 2 частей: маркер файла-источника (query или url) и запрос или URL.
>
> Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id
> пользователя, запрос, URL.

# Sample Input:

user1	query:гугл
user1	url:google.ru
user2	query:стэпик
user2	query:стэпик курсы
user2	url:stepic.org
user2	url:stepic.org/explore/courses
user3	query:вконтакте

# Sample Output:

user1	гугл	google.ru
user2	стэпик	stepic.org
user2	стэпик	stepic.org/explore/courses
user2	стэпик курсы	stepic.org
user2	стэпик курсы	stepic.org/explore/courses
