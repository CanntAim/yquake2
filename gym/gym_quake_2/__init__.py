from gym.envs.registration import register

register(
	id='gym-quake-2-duel-v0',
	entry_point='gym_quake_2.envs:Quake2DuelEnv',
)
