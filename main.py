import pyfiglet
import progressBar
import time
import optparse
import image_steno

def banner():
    """
    A function to print the image-steno banner to stdout.
    """
    
    result = pyfiglet.figlet_format("Image-Steno")
    print(result)


if __name__ == "__main__":
    banner()
    parser = optparse.OptionParser("usage %python main.py -s <souce file> -t <text to hide> -d <destination image> -e <encrypt>")
    parser.add_option('-s', dest='source', type='string',help='The source image to steno.')
    parser.add_option('-t', dest='text', type='string',help='The text to hide')
    parser.add_option('-d', dest='dest', type='string',help='The destination image within which to hide text.')
    parser.add_option('-e', dest='encrypt', type='string',help='Set to true if hiding data, otherwise omit.')
    
    (options, args) = parser.parse_args()
    if options.interface == None:
        print(parser.usage)
        exit(0)

    else:
        steno = image_steno(options.source, options.text, options.dest)

        if (options.encrypt):
             pBar = progressBar.progressBar("Fetching base image.")
             pBar.start()
             time.sleep(2)
             pBar.setMsg("Creating destination image.")
             time.sleep(2)
             pBar.stop()
             time.sleep(0.2)
             steno.hide_text()
        else:
            pBar = progressBar.progressBar("Extracting text.")
            pBar.start()
            time.sleep(2)
            steno.extract_text()
            pBar.stop()
            time.sleep(0.2)