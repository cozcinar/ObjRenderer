import argparse, sys, os
import glob

from pathlib import Path

def run(args, obj, output_folder):
    cmd = "blender-2.79a-linux-glibc219-x86_64/blender --background --python render_blender.py -- --view "
    cmd += str(args.views)
    cmd += obj + " --output_folder " + output_folder
    cmd += " --scale 0.2"
    os.system(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Renders given obj file by rotation a camera around it.')
    parser.add_argument('--views', type=int, default=30,
                    help='number of views to be rendered')
    parser.add_argument('--input_folder', type=str, 
                        help='The path the input will be dumped to.')                    
    parser.add_argument('--output_folder', type=str, default='/tmp',
                        help='The path the output will be dumped to.')
    parser.add_argument('--scale', type=float, default=1,
                        help='Scaling factor applied to model. Depends on size of mesh.')
    parser.add_argument('--remove_doubles', type=bool, default=False,
                        help='Remove double vertices to improve mesh quality.')
    parser.add_argument('--edge_split', type=bool, default=False,
                        help='Adds edge split filter.')
    parser.add_argument('--depth_scale', type=float, default=1.4,
                        help='Scaling that is applied to depth. Depends on size of mesh. \
                            Try out various values until you get a good result. Ignored if format is OPEN_EXR.')
    parser.add_argument('--color_depth', type=str, default='8',
                        help='Number of bit per channel used for output. Either 8 or 16.')
    parser.add_argument('--format', type=str, default='PNG',
                        help='Format of files generated. Either PNG or OPEN_EXR')

    argv = sys.argv[sys.argv.index("--") + 1:]
    args = parser.parse_args(argv)

    BASE_DIR = Path(__file__).resolve().parent

    for i in glob.glob(args.input_folder+'/*/'):

        model_name = i.split('/')[1]
        model_folder = str(BASE_DIR) + '/models/' + model_name
        obj_folder = Path(model_folder + '/rendered').mkdir(parents=True, exist_ok=True)
        
        obj =  Path(model_folder + '/geometry_result/' + model_name + '_obj/' + model_name + '.obj')

        run(args, obj=str(obj), output_folder=model_folder + '/rendered')