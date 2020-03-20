import os
import argparse
def rename_file(path, start_number):
    images = [f for f in os.listdir(path) if not f.startswith('.')]
    for i, img in enumerate(images, start_number):
        _, ext = os.path.splitext(img)
        dst = path + '/' + 'frame_' + str(i) + ext
        temp = path
        path = path + '/' + img
        print('000', path, end='\n')
        print(dst)
        os.rename(path, dst)
        path = temp
# def main():
parse = argparse.ArgumentParser()
parse.add_argument('-p', '--path', help='files path')
parse.add_argument('-n', '--start_number', type=int, help='start number')
args = parse.parse_args()

rename_file(args.path, args.start_number)
# if '__name__' == '__main__':
    # main()