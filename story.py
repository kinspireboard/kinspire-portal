#!/c/Python27/python

import io
import json
import collections

STORY_NUMBERS = 2
CONTENT_FOLDER = 'app/www/content/stories/'


def main():
    '''
    Main routine
    '''
    i = 1
    while i <= STORY_NUMBERS:
        handle_story(i)
        i += 1


def handle_story(i):
    filename = io.open(CONTENT_FOLDER + str(i) +
                       '.json', 'r', encoding='utf8')
    story_json = json.load(filename, object_pairs_hook=collections.OrderedDict)

    generate_story(i, story_json)
    generate_questions(i, story_json)


def generate_story(i, story_json):
    '''
    Creates the story HTML to be injected into the stories page from the respective JSON files.
    '''
    output_file = io.open(
        '{0}story-{1}.html'.format(CONTENT_FOLDER, str(i)), 'w', encoding='utf8')

    paragraphs = story_json['story']
    vocab = story_json['vocab']
    translations = story_json['translation-te']
    i = 0

    for paragraph in paragraphs:
        while i < len(vocab):
            parts = paragraph.split(vocab[i], 1)

            output_file.write(parts[0] + '\n')

            if len(parts) < 2:
                break

            # Write out the vocab word with scaffolding
            output_file.write(u'<span class="stories-vocab">\n')
            output_file.write(
                u'\t<span class="stories-vocab-word">' + vocab[i] + u'</span>')
            output_file.write(u'\t<div class="stories-vocab-def">' + (
                translations[i] if i < len(translations) else '[translation]') + u'</div>')
            output_file.write(u'</span>')
            i += 1

            paragraph = parts[1]

        if i == len(vocab):
            output_file.write(paragraph + '\n')

        # outputFile.write(paragraph)
        output_file.write(u'<br/><br/>')


def generate_questions(i, story_json):
    '''
    Generates the questions HTML from the various json files.
    '''
    output_file = io.open(
        '{0}questions-{1}.html'.format(CONTENT_FOLDER, str(i)), 'w', encoding='utf8')

    questions = story_json['questions']

    for i, question in enumerate(questions):
        output_file.write(u'<li>{0}</li>'.format(question['question']))

        if question['type'] == 'mcq':
            # output_file.write(u'<ol type="a">')
            # output_file.write(u'<form>')

            for j, choice in enumerate(question['choices']):
                output_file.write(
                    u'<div class="radio"><label><input type="radio" name="optradio">{0}</label></div>'.format(choice))

# <div class="radio">
#   <label><input type="radio" name="optradio">Option 2</label>
# </div>
# <div class="radio disabled">
#   <label><input type="radio" name="optradio" disabled>Option 3</label>
# </div>                    u'<input type="radio">&nbsp;{0}<br>'.format(choice))

            # output_file.write(u'</ol>')
            # output_file.write(u'</form>')

        elif question['type'] == 'free':
            output_file.write(
                u'<input type="text" name="question-{0}">'.format(i))


if __name__ == "__main__":
    main()
