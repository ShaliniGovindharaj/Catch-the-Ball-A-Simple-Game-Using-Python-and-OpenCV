import cv2
import numpy as np
import random

ball_radius = 10

# random position (top)
ball_position = [random.randint(ball_radius, 500 - ball_radius), 0]

# falling speed
ball_velocity = [0, random.uniform(50, 7)]

while True:
    # create window every frame
    game_window = np.zeros((500, 500, 3), dtype=np.uint8)

    # move ball down
    ball_position[1] += ball_velocity[1]

    # if ball reaches bottom
    if ball_position[1] >= 500 - ball_radius:
        ball_position = [random.randint(ball_radius, 500 - ball_radius), 0]
        ball_velocity = [0, random.uniform(5, 5)]

    # draw ball
    cv2.circle(
        game_window,
        (int(ball_position[0]), int(ball_position[1])),
        ball_radius,
        (0, 0, 255),
        -1
    )

    # show window
    cv2.imshow("catch the ball", game_window)

    # quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
