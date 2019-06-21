This repo contains the data used for "The Market for Data Privacy" by Tarun Ramadorai, Antoine Uettwiller and Ansgar Walther. 
The data consists of privacy policies, attributes of those policies, 
and measures of third-party sharing behavior
for the sample of firms from Compustat US used in the paper.

The repo further contains Python code which can be used to scrape and clean similar data 
for use in research on other firms and institutions.

If you use either the code or the data, please cite our paper:

@article{ramadorai2019market,
  title={The Market for Data Privacy},
  author={Ramadorai, Tarun and Walther, Ansgar and Uettwiller, Antoine},
  year={2019},
  publisher={CEPR Discussion Paper No. DP13588}
}

# Published Data

Our data is indexed by websites, which can be merged onto the Compustat US data using the *weburl* field in WRDS.

The file *policies.json* contains  
