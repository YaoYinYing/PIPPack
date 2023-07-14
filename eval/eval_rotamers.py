import argparse
import os, glob
from functools import partial
from multiprocessing import Pool, Manager

rotamer_test = "/nas/longleaf/home/nzrandol/kuhl_lab/MolProbity/molprobity/cmdline/rotamer-test"


def _eval_rotamers(pdb_file, out_file, lock):
    # Write clash score to temporary file
    tmp_file = f"tmp_eval_rotamers_{os.getpid()}.txt"
    os.system(f'{rotamer_test} {pdb_file} | grep "\[eval\] =>" > {tmp_file}')
    
    with lock:
        with open(tmp_file, 'r') as f_in, open(out_file, 'a') as f_out:
            eval_lines = f_in.readlines()
            f_out.write(f"{os.path.basename(pdb_file)}:\n") 
            for line in eval_lines:
                f_out.write(f"\t{line.strip()}\n")
    
    
def main(args):
    # Get list of pdb files to evaluate
    pdb_files = glob.glob(os.path.join(args.pdb_dir, '*.pdb'))
    
    # Create the output file
    out_file = os.path.join(args.pdb_dir, "rotamer_evals.txt")
    with open(out_file, 'w') as f:
        f.write("Rotamer Evaluations:\n")

    # Run evaluation
    with Manager() as manager:
        lock = manager.Lock()
        with Pool(args.num_workers) as p:
            p.map(partial(_eval_rotamers, out_file=out_file, lock=lock), pdb_files)
            
    # Clean up
    for f in glob.glob("tmp_eval_rotamers_*.txt"):
        os.remove(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdb_dir', type=str, help='Directory containing pdb files to evaluate.')
    parser.add_argument('--num_workers', type=int, default=4)
    args = parser.parse_args()
    
    main(args)