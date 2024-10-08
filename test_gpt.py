import unittest
from gpt import GPTAnswerer


class TestGPT(unittest.TestCase):

    personal_data_text = """
    John Doe
    123 Main Street
    Anytown, USA 12345
    555-555-5555
    
    ## Skills:
    - Swift and Objective-C
    - iOS frameworks: UIKit, Core Data, and Core Animation
    - Git
    - Microsoft Office
    
    - Willing to relocate
    - Willing to travel
    """

    demo_resume_text = """
    John Doe
    123 Main Street
    Anytown, USA 12345
    555-555-5555
    
    ## Education
    - **Bachelor of Science in Computer Science**  
          Ohio State University, Columbus, Ohio  
          Year of Graduation: 2020

    ## Skills:
    - Proficient in iOS app development using Swift and Objective-C
    - Strong knowledge of iOS frameworks such as UIKit, Core Data, and Core Animation
    
    ## Experience:
    - **iOS Developer**
            ABC Company, Anytown, USA
            January 2019 - Present
            - Developed and maintained 4 iOS apps that are used by thousands of users
            - Worked with the design team to create an app that was featured in the App Store
    
    ## Projects:
    - **Pooping selfie app**
            - Created an app that allows users to take a selfie only while pooping
            - Image recognition algorithm detects if the user is pooping, sees the bathroom, and is wearing pants.
    """

    demo_cover_letter_text = """
    Dear Hiring Manager,
    
    I am writing to apply for the [[position]] position at [[company]]. With a Bachelor of Science in Computer Science and 2 years of experience specializing in iOS app development, I am confident in my ability to contribute to innovative mobile solutions.
    
    I have a strong command of iOS frameworks such as UIKit, Core Data, and Core Animation, and I am proficient in Swift and Objective-C. I have a proven track record of delivering high-quality products, meeting deadlines, and collaborating effectively with cross-functional teams.
    
    I am excited to bring my expertise in developing key features and resolving bugs to your team. Projects like SocialConnect and eShop demonstrate my leadership in implementing user authentication, real-time messaging, and push notifications, as well as integrating RESTful APIs and optimizing app performance with Core Data.
    
    As an Apple Certified iOS Developer, I stay up-to-date with the latest trends and technologies. I possess excellent problem-solving and communication skills, and I am committed to driving the development of cutting-edge mobile solutions.
    
    I am confident that my technical skills and motivation make me an excellent fit at [[company]]. Thank you for considering my application. I have attached my resume and look forward to the opportunity to discuss my qualifications further.
    
    Sincerely,
    John Doe
    """

    demo_job_description_text = """
    
    ## Job Description
    - **iOS Developer** 
    - Company: ZXY Incorporated 
    - Location: Sometown, USA
            
    ## Requirements
    - Proficient in iOS app development using Swift and Objective-C
    - Strong knowledge of iOS frameworks such as UIKit, Core Data, and Core Animation
    - Experience developing iOS apps and working with a team to create an app that was featured in the App Store
    - Word experience is a plus
    
    ## Soft Skills
    - Excellent communication skills
    - Ability to work in a team from home
    
    Travel up to 25% of the time.
    """

    demo_job_description_real_text = """
    Position: iOS Developer
    Company: August
    Location: United Kingdom Remote 
    £60,000/yr - £90,000/yr · Full-time
    
    📱iOS Apple Developer (Senior-range)

    🏝 Remote Working - London office
    
    🇬🇧 UK Based Applicants Only
    
    💵 £60K - £90K+ (DOE - Negotiable further for extraordinary candidates)
    
    August is the disruptive platform allowing one to manage all renting needs in one app. Our All-In-One Solution is the first and only platform designed for both Landlords and Tenants, enabling modern, seamless communication, rental payments, e-contracts management, and more.
    
    We are unique because…
    
    -Open-banking integration, revolutionising rental payment and management.
    
    -User experience is our core priority, we want everything to be as pretty as you :-)
    
    -Our technology brings real automation, providing huge time savings
    
    -A few more things, We’ll tell you more if we like you ;-)
    
    👀 We are Looking for…
    
    Front-End Apple iOS SwiftUI Developer
    3+ years Professional Experience developing in Apple
    Solid understanding of HTTP and WebAPIs with JSON and Swagger
    Proficient & knowledgeable in designing a mobile experience for variable screen sizes for native iOS using SwiftUI
    Strong knowledge of Apple design principles, interface guidelines, patterns, and best practices
    Third party SDKs integration experience eg. Google Firebase, Meta and Facebook SDKs
    Test driven development TDD, logging and crash reporting experience
    🏗 To Do…
    
    Developing, testing, deploying & maintaining applications - creating elegant Mobile UI/UX apple applications.
    Working from user stories and tasks
    Work with back end developers to consume WebAPIs as well as a range of other stakeholders
    Ability to understand & implement business requirements and translate them into technical requirements
    Create and understand secure apps and have a disciplined approach to versioning, releases and environments
    Produce documentation and promote to team
    Work to improve performance across our technological stack
    🙋🏻‍♂️ And You…
    
    Ideally have demonstrable portfolio of previous App work
    Keen eye to detail and elegant mobile UI/UX
    Agile/Scrum way of working and experience, Azure DevOps (ADO) familiarity with repos, pipelines and boards
    Multi-functional, can-do attitude
    As a startup willingness to try/suggest new ideas
    Remote first but meet up occasionally with other team members and the organisation
    The Boring stuff, Benefits, Blah…
    
    🎁Benefits
    
    Pret Coffee Subscription
    Pocket Money, £60 per month (Chocolate, Cigarettes… you decide it's on us!)
    Company Laptop/ Equipments
    x2 Get out of Jail free cards (Hangover/Duvet Days)
    Share Option Scheme
    Pluralsight subscription or training platform of your choice
    📝The Details
    
    Annual Leave 25 days, rising to 29 days (annually)
    Pension Scheme
    Enhanced family friendly policies from day one
    Remote first with occasional London team meetings requirement or hybrid
    Training encouraged/career development from day one
    Regular salary performance/reviews
    Supportive culture with like-minded techies
    """

    demo_job_description_real_text_summary = """
    Company: August
    Location: United Kingdom Remote
    £60,000/yr - £90,000/yr · Full-time
    Role: iOS Developer
    
    ## Requirements
    | Hard Skills | experience |
    | ---------------- | ---------- |
    | Apple Developer | 3+ years Professional Experience |
    | HTTP and WebAPIs | Solid understanding |
    | SwiftUI | Proficient & knowledgeable |
    | Apple design principles | Strong knowledge |
    | Third party SDKs | Integration experience |
    | TDD | Test driven development |
    | Logging and crash reporting | experience |
    
    | Soft Skills | experience |
    | ----------- | ---------- |
    | Agile/Scrum | Way of working and experience |
    | Azure DevOps | Familiarity with repos, pipelines and boards |
    | Multi-functional | Can-do attitude |
    | Willingness to try/suggest new ideas | |
    
    ## More information
    - Developing, testing, deploying & maintaining applications - creating elegant Mobile UI/UX apple applications.
    - Working from user stories and tasks.
    - Work with back end developers to consume WebAPIs as well as a range of other stakeholders.
    - Ability to understand & implement business requirements and translate them into technical requirements.
    - Create and understand secure apps and have a disciplined approach to versioning, releases and environments.
    - Produce documentation and promote to team.
    - Work to improve performance across our technological stack.
    - Ideally have demonstrable portfolio of previous App work.
    - Keen eye to detail and elegant mobile UI/UX.
    - Remote first but meet up occasionally with other team members and the organisation.
    - Benefits include Pret Coffee Subscription, Pocket Money, Company Laptop/ Equipments, Share Option Scheme, Pluralsight subscription or training platform of your choice, Annual Leave 25 days, rising to 29 days, Pension Scheme, Enhanced family friendly policies from day one, Training encouraged/career development from day one, Regular salary performance/reviews, Supportive culture with like-minded techies.
    """

    demo_job_description_real_text_summary_healthcare = """
    Company: VitalCare
    
    Location: United Kingdom (Remote)
    
    £60,000/yr - £90,000/yr · Full-time
    
    Role: iOS Developer
    
    ## About VitalCare
    VitalCare is a leading provider of healthcare solutions, with a focus on improving patient outcomes. We are a fast-growing company with a strong focus on innovation and technology. We are looking for a talented iOS Developer to join our team.
    
    ## Requirements
    
    | Hard Skills                 | Experience              |
    | --------------------------- | ----------------------- |
    | Apple Developer             | 3+ years Professional Experience |
    | HTTP and WebAPIs            | Solid understanding     |
    | SwiftUI                     | Proficient & knowledgeable |
    | Apple design principles     | Strong knowledge        |
    | Third party SDKs            | Integration experience |
    | TDD                         | Test driven development |
    | Logging and crash reporting | Experience              |
    
    | Soft Skills              | Experience              |
    | ------------------------ | ----------------------- |
    | Agile/Scrum              | Way of working and experience |
    | Azure DevOps             | Familiarity with repos, pipelines and boards |
    | Multi-functional         | Can-do attitude         |
    | Willingness to try/suggest new ideas |                   |
    
    ## More information
    
    - Developing, testing, deploying & maintaining applications - creating elegant Mobile UI/UX apple applications for VitalCare, a leading healthcare company.
    - Working from user stories and tasks, ensuring that the developed applications meet the specific needs of the healthcare industry.
    - Collaborating with back-end developers to consume WebAPIs and collaborating with a range of other stakeholders, including healthcare professionals, to gather requirements and deliver high-quality applications.
    - Ability to understand and implement business requirements, translating them into technical requirements for healthcare applications.
    - Creating and understanding secure apps with a strong emphasis on patient data privacy and security. Adhering to disciplined approaches to versioning, releases, and environments.
    - Producing documentation and sharing knowledge with the team, promoting best practices and ensuring efficient collaboration.
    - Striving to improve performance across our technological stack, exploring new tools, frameworks, and methodologies to enhance the development process.
    - Ideally, having a demonstrable portfolio of previous healthcare-related app work, showcasing a keen eye for detail and elegant mobile UI/UX design.
    - Remote-first work environment, but occasional meet-ups with other team members and the organization to foster teamwork and collaboration.
    - Benefits include Pret Coffee Subscription, Pocket Money, Company Laptop/Equipment, Share Option Scheme, Pluralsight subscription or training platform of your choice, Annual Leave 25 days, rising to 29 days, Pension Scheme, Enhanced family-friendly policies from day one, Training encouraged/career development from day one, Regular salary performance/reviews, Supportive culture with like-minded techies.        """

    demo_job_titles_filters = """    
    # About this document
    On this document, explain the rules to filter through job postings. 
    
    Both `# Job Title Filters` and `# Job Description Filters` sections, must be included on the document.
    
    -----
    
    # Job Title Filters
    I'm looking for jobs that are close to (but not exclusively): Senior Developer, Frontend Developer, IOS Developer, Product Manager. Other roles similar to these are also acceptable.

    Also, I'm not interested in junior positions, I'm looking for a mid-level position or higher.
    
    Also there are some industries I'm not interested in: blockchain and healthcare.
    
    # Job Description Filters
    I'm looking for jobs that are close to (but not exclusively): Senior Developer, Frontend Developer, IOS Developer, Product Manager. Other roles similar to these are also acceptable.
    
    I'm not interested in junior positions. I'm looking for a mid-level positions or higher.
    
    I seek responsibilities that are close to (but not exclusively): UX design, product design, agile coding practices, animations, and web APIs usage.
    
    Ideal roles are those where UX/UI design knowledge is required, as well as, experience on agile methodologies, and startup experience. A job not meeting these requirements is still acceptable.
    
    I'm not interested on certain sectors: blockchain, healthcare, health, medicine, or accounting; these sectors are an automatic 'no'. 
    """

    # Set up the answerer
    answerer = GPTAnswerer(demo_resume_text, personal_data_text, demo_cover_letter_text, demo_job_titles_filters)
    # Use a description resume to test the answerer, so we don't have to wait for the resume summary to be generated
    answerer.job_description_summary = demo_job_description_real_text_summary
    # Correct way to do it: answerer.job_description = demo_job_description_real_text

    def test_answer_question_textual_wide_range_name(self):
        question = "What is your name?"
        answer = self.answerer.answer_question_textual_wide_range(question)
        print(f"Name: {answer}")
        self.assertIn("John Doe", answer)

    def test_answer_question_textual_wide_range_phone_number(self):
        question = "What is your phone number?"
        answer = self.answerer.answer_question_textual_wide_range(question)
        print(f"Phone number: {answer}")
        self.assertIn("555-555-5555", answer)

    def test_answer_question_textual_wide_range_experience(self):
        question = "What is the name of the last company you worked at?"
        answer = self.answerer.answer_question_textual_wide_range(question)
        print(f"Experience: {answer}")
        self.assertIn("ABC Company", answer)

    def test_answer_question_textual_wide_range_cover_letter(self):
        question = "Cover Letter"
        answer = self.answerer.answer_question_textual_wide_range(question)
        print(f"Cover letter: {answer}")

        question = "Your message to the hiring manager"
        answer = self.answerer.answer_question_textual_wide_range(question)
        print(f"Your message to the hiring manager: {answer}")

    def test_summarize_job_description(self):
        # summary = self.answerer.job_description_summary                 # It's a computed property
        summary = self.answerer.summarize_job_description(self.demo_job_description_real_text)
        print(f"Summary: \n{summary}")

    def test_answer_question_textual(self):
        question = "What is your name?"
        answer = self.answerer.answer_question_textual(question)
        print(f"Name: {answer}")
        self.assertIn("John Doe", answer)

    def test_answer_question_from_options(self):
        question = "What is your preferred version control?"
        options = ["git", "svn", "mercurial"]
        answer = self.answerer.answer_question_from_options(question, options)
        print(f"{question}, Options {options}. Answer: {answer}")
        self.assertIn("git", answer)

    def test_job_title_passes_filters(self):
        print(f"Testing job title filters. User provided {self.answerer.job_filtering_rules}")
        self.assertTrue(self.answerer.job_title_passes_filters("iOS Developer - MeetKai Metaverse - REMOTE"))
        self.assertFalse(self.answerer.job_title_passes_filters("Nurse"))
        self.assertFalse(self.answerer.job_title_passes_filters("Junior IOS Developer"))
        self.assertFalse(self.answerer.job_title_passes_filters("Junior IOS Developer - 100% Remote"))
        self.assertFalse(self.answerer.job_title_passes_filters("Product Manager - Healthcare"))

    def test_job_description_passes_filters(self):
        self.answerer.job_description_summary = self.demo_job_description_real_text_summary
        self.assertTrue(self.answerer.job_description_passes_filters())

        self.answerer.job_description_summary = self.demo_job_description_real_text_summary_healthcare
        self.assertFalse(self.answerer.job_description_passes_filters())


if __name__ == '__main__':
    unittest.main()
