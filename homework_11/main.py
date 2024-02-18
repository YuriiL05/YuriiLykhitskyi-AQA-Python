# Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм,
# скриття, інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи
import painting
import sculpture

mona_lisa = painting.Painting('Mona Lisa', 'Leonardo Da Vinci', 'Portrait')
venera_miloska = sculpture.Sculpture.from_title('Venera Miloska')
venera_miloska.author = 'Pitochelly'

print(venera_miloska.get_full_info())
print(mona_lisa.get_full_info())
