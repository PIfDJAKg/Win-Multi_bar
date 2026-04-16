from core_tools import executor, detector


def input_data(data):
    executable = detector.detect(data)
    print(executable)
    executor.execute(executable)


def main():
    data = input()
    input_data(data)


if __name__ == "__main__":
    main()