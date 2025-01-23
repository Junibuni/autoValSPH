from validation_test import (
    hydrostatic,
    dambreak,
    periodic_poiseulle,
    obc_poiseuille
)

run_registry = {
    "hydrostatic": hydrostatic.run,
    "dambreak": dambreak.run,
    "periodic_poiseulle": periodic_poiseulle.run,
    "obc_poiseuille": obc_poiseuille.run 
}

globals().update(run_registry)
