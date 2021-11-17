#!/usr/bin/ruby
# This script maintains all the generated endmatter.
# Like feedback links, etc.

require "find"

PROJECT_ROOT = File.expand_path("../..", File.dirname(__FILE__))
REPOSITORY = "devops-course"

START_TAG = "<!-- BEGIN GENERATED SECTION DO NOT EDIT -->"
END_TAG = "<!-- END GENERATED SECTION DO NOT EDIT -->"

def make_contents(path)
  filename = path.sub("#{PROJECT_ROOT}/", "")
  feedback_link = "https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=#{REPOSITORY}&prefill_File=#{filename}&prefill_Sentiment="
  ["\n---",
    "",
    "**How was this resource?**  ",
    "[😫](#{feedback_link}😫) [😕](#{feedback_link}😕) [😐](#{feedback_link}😐) [🙂](#{feedback_link}🙂) [😀](#{feedback_link}😀)  ",
    "Click an emoji to tell us.\n"
  ].join("\n")
end

def update_section(path)
  new_contents = []
  state = :before
  File.foreach(path).each_with_index do |line, lineNo|
    if state == :during and line.strip == END_TAG
      puts "   - Found end tag #{lineNo + 1}."
      state = :after
    end
    if state == :before or state == :after
      new_contents << line
    end
    if state == :before and line.strip == START_TAG
      puts "   - Found start tag #{lineNo + 1}."
      new_contents << make_contents(path) + "\n"
      state = :during
    end
  end
  if state == :before
    puts "   - No start tag found. Appending one..."
    new_contents = new_contents.reverse.drop_while { |element| element.strip.empty? }.reverse
    new_contents << "\n" + START_TAG + "\n"
    new_contents << make_contents(path) + "\n"
    new_contents << END_TAG + "\n"
    File.write(path, new_contents.join)
    puts "   - File written successfully."
  elsif state == :during
    puts "   - No end tag found"
    puts "   - Go fix it and then hit return to retry"
    gets
    update_section(path)
  else
    puts "   - File read successfully. Writing..."
    File.write(path, new_contents.join)
    puts "   - File written successfully."
  end
end

puts PROJECT_ROOT

Find.find(PROJECT_ROOT) do |path|
  next if FileTest.directory? path
  next unless path.downcase.end_with? ".md"
  puts "• Opening File #{path}"
  update_section(path)
end