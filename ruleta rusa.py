import random
bala = random.randint(1,6)
print('Ruleta rusa, el que sobreviva gana')
print('ENTER para precionar el gatillo')
for i in range(1,7):
    input('precinar gatillo')
    if bala == i:
        print('estas muerto')
        art = r'''
          (                                 _
   )                               /=>
  (  +____________________/\/\___ / /|
   .''._____________'._____      / /|/\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \
                    0_0/____/        \
                        |----    /----\
                       || -\\ --|      \
                       ||   || ||\      \
                        \\____// '|      \
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|'''
        print(art)
        break