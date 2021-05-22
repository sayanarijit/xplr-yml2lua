import yaml
from argparse import ArgumentParser, FileType
import sys
import luadata
from flatten_dict.reducers import make_reducer
from flatten_dict import flatten


def main():
    parser = ArgumentParser("xplr-yml2lua")
    parser.add_argument("-i", "--input", type=FileType("r"), default=sys.stdin)
    parser.add_argument("-o", "--output", type=FileType("w"), default=sys.stdout)
    parser.add_argument("-f", "--flat", action="store_true")

    args = parser.parse_args()

    data = yaml.safe_load(args.input.read())

    if args.flat:
        data = flatten(data, reducer=make_reducer(delimiter="."))
        print(
            "\n".join(
                ["{} = {}".format(k, luadata.serialize(v)) for k, v in data.items()]
            )
        )

    else:
        print(
            luadata.serialize(data, indent="  "),
            file=args.output,
        )


if __name__ == "__main__":
    main()
