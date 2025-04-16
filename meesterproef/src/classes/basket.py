class Basket:
    
    def CreateBaskets(self, team1, team2):
        basket = list(range(1, 35))

        colored_balls = ["green_ball", "green_ball", "green_ball", "red_ball", "red_ball", "red_ball"]

        for num in basket:
            if num % 2 != 0:
                team1.basket.append(num)

        for num in basket:
            if num % 2 == 0:
                team2.basket.append(num)

        for colored_ball in colored_balls:
            team1.basket.append(colored_ball)
            team2.basket.append(colored_ball)
            

        print(team1.basket)
        print(team2.basket)
