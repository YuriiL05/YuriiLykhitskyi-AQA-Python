notes = []
command = [
    'add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення',
    'earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої',
    'latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої',
    'longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої',
    'shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої',
    'Exit - вихід'
]

print('Використовуйте наступні команди:')

for line in command:
    print(line)

while True:
    command = input('> ').lower()

    if command == 'exit':
        break
    elif command == 'add':
        note_text = input('> Введіть нотатку: ')
        notes.append(note_text)
    elif command in ['earliest', 'latest', 'longest', 'shortest']:
        sorted_notes = []
        if command == 'earliest':
            sorted_notes = notes.copy()
        elif command == 'latest':
            sorted_notes = notes.copy()
            sorted_notes.reverse()
        elif command == 'longest':
            sorted_notes = sorted(notes, key=lambda x: len(x), reverse=True)
        elif command == 'shortest':
            sorted_notes = sorted(notes, key=lambda x: len(x))

        print(f'Відсортовані нотатки ({command}):')
        if sorted_notes:
            for note in sorted_notes:
                print(f'> {note}')
        else:
            print('Нотатки порожні!')
    else:
        print('Невірна команда! Спробуйте ще раз.')
