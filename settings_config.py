#==============================================================================
# Python Imports
#==============================================================================
import numpy             as np
#==============================================================================

#==============================================================================
class settings:
#==============================================================================
    model = {
        "vp":'Marmousi'   # Circle, Marmousi, GM or GMnew   
            }
#==============================================================================
# Parameters Settings for Homogeneous and Heterogeneous Model
#==============================================================================
    setting1 = {
        "x0": 0.,              # x initial in metters
        "z0": 0.,              # z initial in metters
        "lenpmlx": 200,        # pml lenght x direction  
        "lenpmlz": 200,        # pml lenght z direction 
        "nptx": 201,           # number of points in x-axis
        "nptz": 201,           # number of points in z-axis
        "lenx": 2000,          # x-axis lenght (metters)
        "lenz": 2000,          # z-axis lenght (metters)
        "t0": 0.,              # initial time
        "tn": 1000,            # final time milliseconds
        "cfl": 0.4,            # cfl parameter
        "f0" : 0.01,           # frequency peak kHz
        "Abcs": 'damping',     # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":500,  # shot position from the x0 (metters)
        "shotposition_z":10,   # shot position from the z0 (metters)
        "recposition_x": 20,   # Receiver position from the x0 (metters)
        "recposition_z": 20,   # Receiver position from the z0 (metters)
        "rec_n": 100,          # Receiver number
        "habcw": 2,            # 1=linear , 2=nonlinear weight (used in habc-a1)
        "snapshots": 10,       # wave equation solution snapshots to be saved
        "multiscale": True,    # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8], # frequence band
        "Wavelet_filter": True   # True or False
        }
#==============================================================================

#==============================================================================
# Parameters Settings for GM Model
#==============================================================================
    setting2 = {
        "x0": 26650.,          # x initial in metters
        "z0": 0.,              # z initial in metters
        "lenpmlx": 1500,       # pml lenght x direction  
        "lenpmlz": 700,        # pml lenght z direction
        "nptx": 376,           # number of points in x-axis
        "nptz": 500,           # number of points in z-axis
        "lenx": 15000,         # x-axis lenght (metters)
        "lenz": 7000,          # z-axis lenght (metters)
        "t0": 0.,              # initial time
        "tn": 7000.,           # final time milliseconds
        "cfl": 0.4,            # cfl parameter
        "f0": 0.01,            # frequency peak KHz
        "Abcs": 'pml',         # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":7500, # shot position from the x0 (metters)
        "shotposition_z":32,   # shot position from the z0 (metters)
        "recposition_x": 20,   # Receiver position from the x0 (metters)
        "recposition_z": 32,   # Receiver position from the z0 (metters)
        "rec_n": 376,          # Receiver number
        "habcw": 2,            # 1=linear , 2=nonlinear weight (used in habc-a1)
        "snapshots": 10,       # wave equation solution snapshots to be saved
        "multiscale": True,    # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8],  # frequence band
        "Wavelet_filter": True    # True or False
        }
#==============================================================================

#==============================================================================
# Parameters Settings for GM Model with FWI
#==============================================================================
    setting3 = {
        "x0": 26650.,           # x initial in metters
        "z0": 0.,               # z initial in metters
        "lenpmlx": 1000,        # pml lenght x direction  
        "lenpmlz": 1000,        # pml lenght z direction
        "nptx": 400,            # number of points in x-axis
        "nptz": 400,            # number of points in z-axis
        "lenx": 7000,           # x-axis lenght (metters)
        "lenz": 7000,           # z-axis lenght (metters)
        "t0": 0.,               # initial time
        "tn": 7000.,            # final time milliseconds
        "cfl": 0.4,             # cfl parameter
        "f0": 0.01,             # frequency peak KHz
        "Abcs": 'cpml',         # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":32,    # shot position from the x0 (metters)
        "shotposition_z":32,    # shot position from the z0 (metters)
        "recposition_x": 32,    # Receiver position from the x0 (metters)
        "recposition_z": 32,    # Receiver position from the z0 (metters)
        "rec_n": 300,           # Receiver number
        "habcw": 2,             # 1=linear , 2=nonlinear weight (used in habc-a1)
        "jump": 1,              # Jump to save the wave equation solution to be used in adjoint-based gradient
        "shots_dist":1000,      # distance between the shots in metters
        "USE_GPU_DASK": False,  # True or False
        "threads_per_worker": 1,
        "memory": 70.,           # Restart DASK cluster when more than X% of memory is used
        "dask": True,            # This variable change if you start the DASK cluster
        "death_timeout": 800,    
        "checkpointing":True,    # True or False
        "n_checkpointing": None, # None or an int value n<timestep
        "multiscale": True,      # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8], # frequence band
        "Wavelet_filter": True   # True or False
        }
#==============================================================================

#==============================================================================
# Parameters Settings for Marmousi
#==============================================================================
    setting4 = {
        "x0": 0.,              # x initial in metters
        "z0": 0.,              # z initial in metters
        "lenpmlx": 25,         # pml lenght x direction  
        "lenpmlz": 25,         # pml lenght z direction 
        "nptx": 200,           # number of points in x-axis
        "nptz": 200,           # number of points in z-axis
        "lenx": 250,           # x-axis lenght (metters)
        "lenz": 250,           # z-axis lenght (metters)
        "t0": 0.,              # initial time
        "tn": 350.,            # final time milliseconds
        "cfl": 0.4,            # cfl parameter
        "f0": 0.01,            # frequency peak KHz
        "Abcs": 'pml',         # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":125,  # shot position from the x0 (metters)
        "shotposition_z":125,  # shot position from the z0 (metters)
        "recposition_x": 32,   # Receiver position from the x0 (metters)
        "recposition_z": 2.5,  # Receiver position from the z0 (metters)
        "rec_n": 200,          # Receiver number
        "habcw": 2,            # 1=linear , 2=nonlinear weight (used in habc-a1)
        "jump": 2,             # Jump to save the wave equation solution to be used in adjoint-based gradient
        "shots_dist": 1.25,    # distance between the shots in metters
        "snapshots": 10,       # wave equation solution snapshots to be saved
        "multiscale": True,    # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8],  # frequence band
        "Wavelet_filter": True    # True or False
        }   
#==============================================================================

#==============================================================================
# Parameters Settings for Marmousi with FWI
#==============================================================================
    setting5 = {
        "x0": 0.,                # x initial in metters
        "z0": 0.,                # z initial in metters
        "lenpmlx": 200,          # pml lenght x direction 
        "lenpmlz": 200,          # pml lenght z direction 
        "nptx": 1200,            # number of points in x-axis
        "nptz": 1200,            # number of points in z-axis
        "lenx": 2000,            # x-axis lenght (metters)
        "lenz": 2000,            # z-axis lenght (metters)
        "t0": 0.,                # initial time
        "tn": 2000.,             # final time milliseconds
        "cfl": 0.4,              # cfl parameter
        "f0": 0.005,             # frequency peak KHz
        "Abcs": 'cpml',          # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":125,    # shot position from the x0 (metters)
        "shotposition_z":1.25,   # shot position from the z0 (metters)
        "recposition_x": 2.25,   # Receiver position from the z0 (metters)
        "recposition_z": 2.25,   # Receiver position from the z0 (metters)
        "rec_n": 200,            # Receiver number
        "habcw": 2,              # 1=linear , 2=nonlinear weight (used in habc-a1)
        "jump": 1,               # Jump to save the wave equation solution to be used in adjoint-based gradient
        "shots_dist": 500,       # distance between the shots in metters
        "snapshots": 10,         # wave equation solution snapshots to be saved  
        "USE_GPU_DASK": False,   # True or False
        "threads_per_worker": 1,
        "memory": 70.,           # Restart DASK cluster when more than X% of memory is used
        "dask": True,            # This variable change if you start the DASK cluster
        "death_timeout": 800,    
        "checkpointing":True,    # True or False
        "n_checkpointing": 400,  # None or an int value n<timestep
        "multiscale": True,      # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8], # frequence band
        "Wavelet_filter": True   # True or False
        }
#==============================================================================

#==============================================================================
# Parameters Settings for FWI with Circle
#==============================================================================
    setting6 = {
        "x0": 0.,                # x initial in metters
        "z0": 0.,                # z initial in metters
        "lenpmlx": 100,          # pml lenght x direction
        "lenpmlz": 100,          # pml lenght z direction
        "nptx": 300,             # number of points in x-axis
        "nptz": 300,             # number of points in z-axis
        "lenx": 500,             # x-axis lenght (metters)
        "lenz": 500,             # z-axis lenght (metters)
        "t0": 0.,                # initial time
        "tn": 500,               # final time milliseconds
        "f0" : 0.015,            # frequency peak kHz
        "Abcs": 'Higdon',        # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_z":30,     # shot position from the z0 (metters)
        "recposition_z": 20,     # Receiver position from the z0 (metters)
        "rec_n": 200,            # Receiver number
        "habcw": 2,              # 1=linear , 2=nonlinear weight (used in habc-a1)
        "jump": 1,               # Jump to save the wave equation solution to be used in adjoint-based gradient
        "shots_dist":120,        # distance between the shots in metters
        "USE_GPU_DASK": False,   # True or False
        "threads_per_worker": 1,
        "memory": 70.,           # Restart DASK cluster when more than X% of memory is used
        "dask": False,           # This variable change if you start the DASK cluster
        "death_timeout": 800,    
        "checkpointing":False,   # True or False
        "n_checkpointing": 20,   # None or an int value n<timestep
        "multiscale": True,      # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8], # frequence band
        "Wavelet_filter": True   # True or False
        }
#==============================================================================

#==============================================================================
# Parameters Settings
#==============================================================================
    setting7 = {
        "x0": 1000.,             # x initial in metters
        "z0": 0.,                # z initial in metters
        "lenpmlx": 1000,         # pml lenght x direction 
        "lenpmlz": 1000,         # pml lenght z direction 
        "nptx": 758,             # number of points in x-axis
        "nptz": 400,             # number of points in z-axis
        "lenx": 7462.5,          # x-axis lenght (metters)
        "lenz": 7992.0,          # z-axis lenght (metters)
        "t0": 0.,                # initial time
        "tn": 8000.,             # final time milliseconds
        "cfl": 0.4,              # cfl parameter
        "f0": 0.005,             # frequency peak KHz
        "Abcs": 'cpml',          # Abcs methods, options=damping, pml, cpml, habc-a1, Higdon
        "shotposition_x":125,    # shot position from the x0 (metters)
        "shotposition_z":7.5,    # shot position from the z0 (metters)
        "recposition_x": 2.25,   # Receiver position from the z0 (metters)
        "recposition_z": 12,     # Receiver position from the z0 (metters)
        "rec_n": 300,            # Receiver number
        "habcw": 2,              # 1=linear , 2=nonlinear weight (used in habc-a1)
        "jump": 1,               # Jump to save the wave equation solution to be used in adjoint-based gradient
        "shots_dist": 500,       # distance between the shots in metters
        "snapshots": 10,         # wave equation solution snapshots to be saved  
        "USE_GPU_DASK": False,   # True or False
        "threads_per_worker": 1,
        "memory": 70.,           # Restart DASK cluster when more than X% of memory is used
        "dask": False,           # This variable change if you start the DASK cluster
        "death_timeout": 800,    
        "checkpointing":False,   # True or False
        "n_checkpointing": 400,  # None or an int value n<timestep
        "multiscale": True,      # Frequency multiscale: True or False
        "freq_bands": [2, 5, 8], # frequence band
        "Wavelet_filter": True   # True or False
        }
#==============================================================================