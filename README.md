<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![MIT License][license-shield]][license-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project">
    <img src="static/ipl-logo.png" alt="Logo" width="300" height="200">
  </a>

<h3 align="center">IPL 2023 Powerplay Prediction - Linear Regression ML Project</h3>

  <p align="center">
    The aim of this project is to predict the runs that will be scored in the powerplay of each innings, given the infomration of the venue, batting an bowling team for that innings, and the players which participated in the given overs.
    <br />
    <br />
    <a href="https://ipl-powerplay-prediction.streamlit.app/">View Demo</a>
    ·
    <a href="https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#data-description">Data Description</a>
      <ul>
        <li><a href="#evaluation-metric">Evaluation Metric</a></li>
      </ul>
    </li>
    <li><a href="#models-evaluated">Models Evaluated</a></li>
    <li><a href="#final-test-error">Final Test Error</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

In this machine learning project, the goal is to predict the powerplay runs scored in each inning of IPL matches using linear regression algorithms. The predictive model leverages information such as venue details, batting and bowling team compositions for each inning, and the participation of specific players in designated overs. 

The training dataset consists of two files, namely "IPL_Ball_by_Ball_2008_2022.csv" and "IPL_Matches_Result_2008_2022.csv," providing a comprehensive ball-by-ball record and match results from 2008 to 2022. The mean absolute error (MAE) serves as the evaluation metric for model performance. 

Various regression models, including Ridge, Lasso, Linear Regression, SGD Regressor, Bayesian Ridge, Kernel Ridge, HistGradientBoostingRegressor, MLPRegressor, ExtraTreesRegressor, BaggingRegressor, RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, XGBRegressor, and LGBMRegressor, were evaluated. 

Ultimately, the Stacking Regressor emerged as the chosen model for predictions due to its lower MAE on the training dataset, despite a slightly higher error on the test dataset. The final test error, measured by MAE, stands at 8.579578436102235.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![pandas][Pandas]][Pandas-url]
* [![scikit-learn][scikit-learn]][scikit-learn-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Data Description -->
## Data Description

1. **Training data**: You will be provided two files for training data, they are as following:
    * **IPL_Ball_by_Ball_2008_2022.csv**: This file contains a ball by ball record of each IPL match since 2008 to 2022. The column names are self explanatory. 
    * **IPL_Matches_Result_2008_2022.csv**: This file contains results of each IPL match since 2008 to 2022. The column names are self explanatory. 

The data can be found in the link given [here](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset).

### Evaluation Metric
Here, the data has been evaluated using mean absolute error. The choice of the mean absolute error (MAE) as the evaluation metric for regression problems is rooted in its intuitive and straightforward interpretation. MAE calculates the average absolute differences between predicted and actual values, providing a clear and easily understandable measure of the model's accuracy. 

Unlike other metrics such as mean squared error (MSE), MAE does not heavily penalize large errors, making it more robust to outliers and ensuring that each prediction's impact on the overall evaluation is proportional to its magnitude.This property makes MAE particularly suitable for regression scenarios where the emphasis is on understanding the average magnitude of prediction errors without being overly influenced by extreme values. 

In essence, the simplicity and resilience of MAE make it a reliable choice for assessing the predictive performance of regression models in a manner that aligns with a practical understanding of the errors.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Below given are some additional screenshots of multiple pages of the application which can be accessed based on the basis of the level of control i.e. Admin, Store Manager or User.

1) <strong>Admin</strong>
    [![Product Admin Dashboard Screen Shot][product-admin-dashboard-screenshot]](https://example.com)
    - Above given is the admin dashboard, from where the admin can :
        - Perform the CRUD operations on the categories
        - Manage pending category requests made by the store managers
        - Select the preference of the monthly user report
        [![Product Admin Monthly Report Screen Shot][product-admin-monthly-report-screenshot]](https://example.com)
2) <strong>Store Manager</strong>
    [![Product Manager Dashboard Screen Shot][product-manager-dashboard-screenshot]](https://example.com)
    - Above given is the store manager dashboard, from where the managers can :
        - Perform the CRUD operations on the products
        - Creating and sending category requests to the admins
        - Generate the products csv and receive the same on registered mail
        [![Product CSV Report Screen Shot][product-csv-report-screenshot]](https://example.com)
3) <strong>User</strong>
    [![Product User Dashboard Screen Shot][product-user-dashboard-screenshot]](https://example.com)
    - Above given is the user dashboard, from where the user can :
        - Sort products based on filters and/or categories
        - Buy products from one and/or multiple categories
        - View cart and continue with completing the purchase
        - Viewing the order history


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

I'm thrilled to have you exploring my project! This endeavor is a collective effort, and we believe that every contribution adds value and creativity to our community.

How You Can Contribute:

🛠️ Found a bug? Have an idea for improvement? Fork the repo and create a pull request.

💡 Have a suggestion for making this project even better? Open an issue with the "enhancement" tag.

⭐ Like what you see? Show your support by giving our project a star!

Remember, your contributions, whether big or small, are incredibly valuable to us. They help us learn, inspire, and create a better project together.


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Thank you for being a part of this journey!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Dhruv Pamneja - dpamneja@gmail.com / 21f1001719@ds.study.iitm.ac.in

Project Link: [https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project](https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project.svg?style=for-the-badge
[contributors-url]: https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project.svg?style=for-the-badge
[forks-url]: https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/network/members
[stars-shield]: https://img.shields.io/github/stars/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project.svg?style=for-the-badge
[stars-url]: https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project.svg?style=for-the-badge
[issues-url]: https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/issues
[license-shield]: https://img.shields.io/github/license/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project.svg?style=for-the-badge
[license-url]: https://github.com/d-pamneja/IPL2023_PowerPlay_Linear_Regression_Project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dhruv-pamneja-3b8432187/
[product-screenshot]: static/app_ss.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org
[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/stable/
