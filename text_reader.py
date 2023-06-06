def main():
    import threading
    from ES.GUI import run_text_reader
    import ES.test as test
    from ES.driver import tech

    def new(arg):
        run_text_reader(arg)
    # text_reader_thread = threading.Thread(target=new, args=(tech))
    text_reader_thread = threading.Thread(target=run_text_reader)

    # Start the Text Reader GUI thread
    text_reader_thread.start()

    # Call another_function() concurrently
    test.run()

if __name__ == "__main__":
    main()
