player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemies = [
    {
        'name': 'Arnolde', 
        'hp': 10,
        'attack': 10,
        'script': 'Почему ты тут? Уходи, пока можешь. ',
        'win': 'Ты - достойный противник, но алмазы все равно будут моими.',
        'loss': 'хаахаххха, больше не позорься, тебе ещё рано с кем либо сражаться.'
    },
    {
        'name': 'Chicago',
        'hp': 20,
        'attack': 25,
        'script': 'я не думал что нам сужденно будет встретиться)) не особо люблю говорить,поэтому приступим к делу!',
        'win': 'КАК?ладно мне не о чем с тобой говорить.',
        'loss': 'я знал итог нашего сражения! зря время тратил попусту'
    },

    {
        'name': 'Rima',
        'hp': 200,
        'attack': 50,
        'script': 'о,нвый сопернииииик!!!!ну чего мы ждем????',
        'win': 'эх...',
        'loss': 'ДА! Я ЭТО СДЕЛАЛАААА!!!!!!'
    }
]


items = {
    '1': {
        'name': 'Зелье удачи',
        'price': 1500
    },
    '2': {
        'name': 'Пропуск тренировки',
        'price': 1000
    }
}

