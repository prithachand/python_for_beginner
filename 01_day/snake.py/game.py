diff --git a/README.md b/README.md
index 68ecd6f2ff75b20ecf899633a8ea674d121fc208..1fffd6be1ee7b79f59110b2b44513957bb4afdd0 100644
GIT binary patch
literal 656
zcmZ{iK~KU!6olu@uV})(7jND?7(Hl01kZHQT8KaiR7wB5`psKvy_lx$c4ywanYaD^
znyS#f7JAf!mU>gGBkz@JHQH#;RkL%_B(AB<pQ%@;HQYU4bDl}>@Cx0r+OabGhVK&^
zI~}wQ^e?lyFbfzbm`R`98<>gineYCED)6Dh5?8rHiE0m4!g$h0FgLg=bVkMQuERwI
zr$RBIvS!CsgZC@g|7%a8vI>=Fc+TfazY{Y#lK;%w$$N04Ezg&jOBeVyc5}_x$)0b~
zuv<^O)obuv-TdlqL#ILg$bKTBS#|XGTn^x#P)BboE-v1N37P8}J39yFsv*JXrU3KA
z@+p{`n7^I-U-0>4%xSH#3cr2yoWZE6bnP5RiS&6+&XTb%96M_wZ3k}E(PhiYd#_~D
EKhRln@Bjb+

delta 10
RcmbQhsy9K4g_nVg0RRk-0hs^*

diff --git a/snake_game.py b/snake_game.py
new file mode 100644
index 0000000000000000000000000000000000000000..8d0f7e23c3fc32178c262db4301dc4c15794ed5c
--- /dev/null
+++ b/snake_game.py
@@ -0,0 +1,214 @@
+"""A simple Snake game built with Python's standard tkinter library.
+
+Run with:
+    python3 snake_game.py
+
+Controls:
+    Arrow keys - change direction
+    Space      - restart after game over
+"""
+
+from __future__ import annotations
+
+import random
+import tkinter as tk
+from dataclasses import dataclass
+
+
+CELL_SIZE = 20
+GRID_WIDTH = 30
+GRID_HEIGHT = 22
+START_SPEED_MS = 130
+MIN_SPEED_MS = 55
+SPEED_STEP = 5
+SCORE_PER_FOOD = 10
+
+BACKGROUND_COLOR = "#101820"
+SNAKE_COLOR = "#31d843"
+SNAKE_HEAD_COLOR = "#5dff6f"
+FOOD_COLOR = "#ff4d4d"
+TEXT_COLOR = "#ffffff"
+
+
+@dataclass(frozen=True)
+class Point:
+    """A position on the grid."""
+
+    x: int
+    y: int
+
+
+class SnakeGame:
+    """Main game controller for Snake."""
+
+    def __init__(self) -> None:
+        self.root = tk.Tk()
+        self.root.title("Snake Game")
+        self.root.resizable(False, False)
+
+        self.canvas_width = GRID_WIDTH * CELL_SIZE
+        self.canvas_height = GRID_HEIGHT * CELL_SIZE
+        self.canvas = tk.Canvas(
+            self.root,
+            width=self.canvas_width,
+            height=self.canvas_height,
+            bg=BACKGROUND_COLOR,
+            highlightthickness=0,
+        )
+        self.canvas.pack()
+
+        self.root.bind("<Up>", lambda _event: self.change_direction(Point(0, -1)))
+        self.root.bind("<Down>", lambda _event: self.change_direction(Point(0, 1)))
+        self.root.bind("<Left>", lambda _event: self.change_direction(Point(-1, 0)))
+        self.root.bind("<Right>", lambda _event: self.change_direction(Point(1, 0)))
+        self.root.bind("<space>", lambda _event: self.restart_if_game_over())
+
+        self.snake: list[Point] = []
+        self.direction = Point(1, 0)
+        self.next_direction = Point(1, 0)
+        self.food = Point(0, 0)
+        self.score = 0
+        self.speed_ms = START_SPEED_MS
+        self.game_over = False
+
+        self.reset_game()
+
+    def reset_game(self) -> None:
+        """Start a new game with the snake in the middle of the screen."""
+        center = Point(GRID_WIDTH // 2, GRID_HEIGHT // 2)
+        self.snake = [
+            center,
+            Point(center.x - 1, center.y),
+            Point(center.x - 2, center.y),
+        ]
+        self.direction = Point(1, 0)
+        self.next_direction = Point(1, 0)
+        self.score = 0
+        self.speed_ms = START_SPEED_MS
+        self.game_over = False
+        self.food = self.random_food_position()
+        self.draw()
+        self.root.after(self.speed_ms, self.game_loop)
+
+    def random_food_position(self) -> Point:
+        """Place food randomly on a free cell."""
+        free_cells = [
+            Point(x, y)
+            for x in range(GRID_WIDTH)
+            for y in range(GRID_HEIGHT)
+            if Point(x, y) not in self.snake
+        ]
+        return random.choice(free_cells)
+
+    def change_direction(self, new_direction: Point) -> None:
+        """Change snake direction, ignoring direct reverse moves."""
+        if self.game_over:
+            return
+
+        is_reverse = (
+            new_direction.x == -self.direction.x
+            and new_direction.y == -self.direction.y
+        )
+        if not is_reverse:
+            self.next_direction = new_direction
+
+    def game_loop(self) -> None:
+        """Update snake movement and redraw until the game ends."""
+        if self.game_over:
+            return
+
+        self.direction = self.next_direction
+        head = self.snake[0]
+        new_head = Point(head.x + self.direction.x, head.y + self.direction.y)
+
+        if self.hit_wall(new_head) or self.hit_self(new_head):
+            self.end_game()
+            return
+
+        self.snake.insert(0, new_head)
+
+        if new_head == self.food:
+            self.score += SCORE_PER_FOOD
+            self.speed_ms = max(MIN_SPEED_MS, START_SPEED_MS - (self.score // 50) * SPEED_STEP)
+            self.food = self.random_food_position()
+        else:
+            self.snake.pop()
+
+        self.draw()
+        self.root.after(self.speed_ms, self.game_loop)
+
+    def hit_wall(self, point: Point) -> bool:
+        """Return True if the snake's head has collided with a wall."""
+        return not (0 <= point.x < GRID_WIDTH and 0 <= point.y < GRID_HEIGHT)
+
+    def hit_self(self, point: Point) -> bool:
+        """Return True if the snake's head has collided with its own body."""
+        return point in self.snake
+
+    def end_game(self) -> None:
+        """Show game-over text and wait for the player to restart."""
+        self.game_over = True
+        self.draw()
+        self.canvas.create_text(
+            self.canvas_width // 2,
+            self.canvas_height // 2 - 20,
+            text="Game Over",
+            fill=TEXT_COLOR,
+            font=("Arial", 28, "bold"),
+        )
+        self.canvas.create_text(
+            self.canvas_width // 2,
+            self.canvas_height // 2 + 20,
+            text="Press Space to play again",
+            fill=TEXT_COLOR,
+            font=("Arial", 14),
+        )
+
+    def restart_if_game_over(self) -> None:
+        """Restart the game when Space is pressed after game over."""
+        if self.game_over:
+            self.reset_game()
+
+    def draw(self) -> None:
+        """Draw the current game state on the canvas."""
+        self.canvas.delete("all")
+        self.draw_food()
+        self.draw_snake()
+        self.draw_score()
+
+    def draw_food(self) -> None:
+        """Draw the food square."""
+        self.draw_cell(self.food, FOOD_COLOR)
+
+    def draw_snake(self) -> None:
+        """Draw the snake body and head."""
+        for index, segment in enumerate(self.snake):
+            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
+            self.draw_cell(segment, color)
+
+    def draw_score(self) -> None:
+        """Draw the current score."""
+        self.canvas.create_text(
+            10,
+            10,
+            text=f"Score: {self.score}",
+            fill=TEXT_COLOR,
+            font=("Arial", 12, "bold"),
+            anchor="nw",
+        )
+
+    def draw_cell(self, point: Point, color: str) -> None:
+        """Draw one grid cell."""
+        x1 = point.x * CELL_SIZE
+        y1 = point.y * CELL_SIZE
+        x2 = x1 + CELL_SIZE
+        y2 = y1 + CELL_SIZE
+        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=BACKGROUND_COLOR)
+
+    def run(self) -> None:
+        """Start the tkinter event loop."""
+        self.root.mainloop()
+
+
+if __name__ == "__main__":
+    SnakeGame().run()
