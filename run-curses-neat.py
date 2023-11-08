import random
import curses
import itertools
import math
import time

from neat.config import Config
from neat.genes import DefaultNodeGene
from neat.genome import DefaultGenome
from neat.nn import FeedForwardNetwork
from neat.population import Population
from neat.reproduction import DefaultReproduction
from neat.species import DefaultSpeciesSet
from neat.stagnation import DefaultStagnation

c = Config(
    DefaultGenome,
    DefaultReproduction,
    DefaultSpeciesSet,
    DefaultStagnation,
    "simple.conf",
)
p = Population(c)

stdscr = curses.initscr()                # 画面を初期化する    

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = FeedForwardNetwork.create(genome, config)

        # ================ ドメインに依存する処理を実装する ==========
        ch = random.choice(["😃", "😍", "🍪"])   # どれかを表示する
        stdscr.addch(0, 0, ch)                   # 1文字表示
        stdscr.addstr(0, 2, " < Hello, world!")  # 文字列を表示する
        stdscr.refresh()                         # 画面の変更を反映する
        genome.fitness = 1  # その個体がどれぐらい、イケてたか？
        time.sleep(0.1)     # 表示を見るため少しスリープする
        # ================ ドメインに依存する処理ここまで ===========

winner = p.run(eval_genomes, n=10)  # 10世代
curses.endwin()  # ゲーム画面の終了
print(winner)        
