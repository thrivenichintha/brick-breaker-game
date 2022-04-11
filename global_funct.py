
def create_header():
    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(global_var.mando.score()) + "   |  COINS: " + str(global_var.mando.coins()) + "   |  LIVES: " + str(global_var.mando.lives()) + "   |  TIME: " +str(global_var.TIME_REM))  .center(config.columns), end='')
    print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.mp.render()

def create_board():

    i = 1
    x = 10

    
    while x < global_var.mp.width - 250:

        no = random.randint(0, 3)
        y = random.randint(10, global_var.mp.height-15)
        
        #beams
        enemy = objects.Object(config.enemy[no], x, y)
        global_var.beams.append(enemy)
        enemy.render()
        
        #dragon power up
        if i % 10 == 0:
            dg_pow_up = objects.Object(config.dg_pow_up, x + 15 , y)
            global_var.dg_power_up.append(dg_pow_up)
            dg_pow_up.render()

        #magnets
        elif i % 5 == 0:
            magnet = objects.Object(config.magnet, x + 10 , y)
            global_var.magnets.append(magnet)
            magnet.render()
        
        i += 1
        x += random.randint(20, 30)
        if x > global_var.mp.width - 250:
            break
            
        y = random.randint(10, global_var.mp.height-15)

        #coins
        coin = objects.Object(config.coins, x, y)
        global_var.coins.append(coin)
        coin.render()


        x += random.randint(20, 30)
        y = random.randint(10, global_var.mp.height-15)
        
        #boost
        boost = objects.Object(config.boost, x, y)
        global_var.boosts.append(boost)
        boost.render()

        x += random.randint(20, 50)



def initialize_board():

    create_board()
    print_board()

