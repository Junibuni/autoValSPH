from validation_test import (
    VAL_Dam_Break,
    VAL_Hydro_Static,
    VAL_OBC_Poiseuille,
    VAL_Periodic_Poiseuille
)

run_registry = {
    "hydrostatic": VAL_Hydro_Static.run,
    "dambreak": VAL_Dam_Break.run,
    "periodic_poiseulle": VAL_Periodic_Poiseuille.run,
    "obc_poiseuille": VAL_OBC_Poiseuille.run 
}

globals().update(run_registry)
