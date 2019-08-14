import argparse


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='Load all ttls in a directory')
    parser.add_argument('--dir', dest='working_directory',
                        help='The directory that holds the ttl files')

    args = parser.parse_args()
    print(args.working_directory)


if __name__ == '__main__':
    main()

