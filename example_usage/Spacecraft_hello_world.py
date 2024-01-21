'''
AWP | Astrodynamics with Python by Alfonso Gonzalez
https://github.com/alfonsogonzalez/AWP
https://www.youtube.com/c/AlfonsoGonzalezSpaceEngineering

Hello world of Spacecraft class
Two-body propagation with J2 perturbation for 100 periods
'''

# Python standard libraries
# AWP libraries
from Spacecraft import Spacecraft as SC
from planetary_data import earth

if __name__ == '__main__':
	coes1 = [ earth[ 'radius' ] + 10000, 0, 90.0, 0.0, 0.0, 0.0 ]
	coes2 = [ earth[ 'radius' ] + 20000, 0, 60.0, 0.0, 0.0, 180.0 ]
	sc1   = SC(
			{
			'coes'       : coes1,
			'tspan'      : '1',
			'dt'         : 100.0,
			'orbit_perts': { 'J2': True }
			} )
	sc2   = SC(
			{
			'coes'       : coes2,
			'tspan'      : '1',
			'dt'         : 100.0,
			'orbit_perts': { 'J2': True }
			} )
	sc1,sc2.plot_3d()
