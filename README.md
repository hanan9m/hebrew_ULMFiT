# hebrew_ULMFiT
Universal Language Model Fine-tuning for Text Classification in Hebew, plus bunus

i happy to share the weight to the hebew ULMFiT model.<br>
ULMFiT published by Jeremy Howard and Sebastian Ruder [here](https://arxiv.org/abs/1801.06146), and touch in [Fast.ai](https://course.fast.ai/) course.<br>
this model is very strong, because he can be easily tranfer to any kind of classification you want.<br>
the hebrew wikipedia dowload from professor Yoav Golberg [web](http://u.cs.biu.ac.il/~yogo/hebwiki/). <br>
download hebew models: [here](https://www.dropbox.com/s/cuefrjm8h5eiirk/wiki-heb.pkl?dl=0)


* wiki training <br>
  1.  hebrew_wiki_part_1.ipynb <br>
      trainaing on wiki from scrach. <br><br>
  2. hebrew_wiki_part_2.ipynb<br>
     remove unwanted chart and retrain.
  
* Bonus - amit segal models. <br>
  1.  amit_segal_data.ipynb <br>
      collect amit segal data <br> <br>
  2.  amit_segal_language_model.ipynb <br>
      train a language model on this corpus. <br><br>
  3.  amit_classification.ipynb <br>
      tranfer the model to make classification between correct and wrong sentence. <br>
      the model achive 0.68 accuracy, which is impressing because the data size & the possible that sentence look <br>
      real (because good predict) and the other side.<br><br>

* load pre-train models and word map <br>
load_models_word_map.ipynb  
after all the model are create, simple load the models, and create word map (with the embedding) from wiki and amit models.
