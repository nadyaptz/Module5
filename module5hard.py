from time import sleep


class User:
    '''
    Класс пользователя User, имеющий атрибуты: ник, пароль (в хэшированном виде) и возраст.
    '''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    '''
    Класс пользователя Video, имеющий атрибуты: title, duration, time_now, adult_mode.
    '''

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now  # место начала просмотра
        self.adult_mode = adult_mode  # по умолчанию False, то есть нет ограничений

    def __eq__(self, other):  # два видео одинаковы, если одинаковы их названия
        if self.title == other.title:
            return True


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):  # проверяем, если пользователь с таким ИМЕНЕМ существует
        if len(self.users) != 0:
            for i in range(0, len(self.users)):
                if self.users[i].nickname == item.nickname:
                    # print(f'Пользователь {item.nickname} уже существует!!!')
                    return True
                else:
                    # print(f'Пользователя {item.nickname} еще не существует')
                    return False

    def log_in(self, nickname, password):  # пользователь с логином и паролем логинится

        if len(self.users) != 0:
            for i in range(0, len(self.users)):
                if self.users[i].nickname == nickname and self.users[i].password == hash(password):
                    self.current_user = self.users[i]
                    # print(f'Пользователь {self.current_user.nickname} залогинился!!!')
                    return True
                else:
                    print(f'Имя пользователя или пароль неверный')
                    break

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):  # регистрация пользователя с логином, паролем и возрастом
        user = User(nickname, password, age)
        if len(self.users) == 0:
            self.users.append(user)
            self.current_user = user
        else:
            if self.__contains__(user):
                print(f'Пользователь {nickname} уже существует')
            else:
                self.users.append(user)
                self.current_user = user

    def get_videos(self, search_string):  # ищем все видео, в названии которых встречается поисковая строка search string
        list_of_videos = []
        for i in range(0, len(self.videos)):
            if search_string.upper() in str.upper(self.videos[i].title):
                list_of_videos.append(self.videos[i].title)
        return list_of_videos

    def add(self, *args):  # добавляем произвольное количество видео в список видео
        for arg in args:
            if arg not in self.videos:
                self.videos.append(arg)

    def watch_video(self, video_title: str):

        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in range(0, len(self.videos)):
                if self.videos[i].title == video_title:
                    current_time = self.videos[i].time_now
                    if self.videos[i].adult_mode:
                        if self.current_user.age < 18:
                            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                        else:
                            self.__watch_video(current_time, i)
                            break
                    else:
                        self.__watch_video(current_time, i)

    def __watch_video(self, current_time, i):
        while current_time <= self.videos[i].duration:
            print(current_time, end=" ")
            sleep(1)
            current_time += 1
        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#v2 = Video('Для чего девушкам парень программист?', 10)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
