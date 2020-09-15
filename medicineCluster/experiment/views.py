from django.shortcuts import render
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd
import urllib



def index(request):
    context={
      "first_page":True
    }
    return render(request, "index.html",context )


def tfidf(request):

  #I gave csv path from my root. in server ı gave from server root 
  df = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/cluster.csv')
  df_2 = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/most_words_list.csv')
  df_3 = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/file_name_cluster_name.csv')
  df_3['cluster'] = df_3['cluster'].astype(str)  #cluster converthing string

  df_3=df_3.iloc[:, 1:]
  df_3['names'] = df_3['names'].apply(lambda x: x.split(".")[0]).astype(int)

  #df_3['names']=df['names'].astype(int)
  df_3 = df_3.groupby('cluster')


  df['cluster'] = df['cluster'].astype(str)  #cluster cahangeing string

 
  #plottinG 2D
  plot_div = plot(px.scatter(df, x="pca_0", y="pca_1",size_max=20,
                 size="max_tfidf_value",hover_data=["name",'cluster',"max_tfidf_value","word_of_max_tfidf"], color="cluster",  template="simple_white",width=900, height=600),
               output_type='div')

  #plottin 3D
  plot_div_3d = plot( px.scatter_3d(df, x="pca_0", y="pca_1",z="pca_2",
              color='cluster',hover_data=["name",'cluster',"max_tfidf_value","word_of_max_tfidf"],template="simple_white", width=950, height=650),
               output_type='div')




  context={'plot_div': plot_div,
   "plot_div_3d":plot_div_3d,
   "Cluster_0":  df_2["Cluster :0"].head(),
   "Cluster_1":  df_2["Cluster :1"].head(),
   "Cluster_2":  df_2["Cluster :2"].head(),
  
   "Cluster_0_fileName":   df_3.get_group('0'),#df_3.get_group('0').head(10),
   "Cluster_1_fileName":   df_3.get_group('1'),#df_3.get_group("1").head(10),
   "Cluster_2_fileName":   df_3.get_group('2'),#df_3.get_group("2").head(10),


   
   "Cluster_0_links":   df_3.get_group('0')["names"].values.tolist(),#df_3.get_group('0').head(10),
   "Cluster_1_links":   df_3.get_group('1')["names"].values.tolist(),#df_3.get_group("1").head(10),
   "Cluster_2_links":   df_3.get_group('2')["names"].values.tolist(),#df_3.get_group("2").head(10),


   "Number_of_cluster_member":[ len(df_3.get_group('0')),
                                len(df_3.get_group('1')),
                                len(df_3.get_group('2')),
                              ],
    "name":"According to TF-IDF",
     "data":df.iloc[:, 1:4].values.tolist()

   }

  return render(request, "index.html",context )
    



def countvc(request):

  #I gave csv path from my root. in server ı gave from server root 
  df = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/cluster_2.csv')
  df_2 = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/most_words_list_2.csv')
  df_3 = pd.read_csv(r'C:/Users/selah/Desktop/2020Staj/medicineCluster/static/data/file_name_cluster_name_2.csv')
  df_3['cluster'] = df_3['cluster'].astype(str)  #cluster converthing string



  df_3=df_3.iloc[:, 1:]
  df_3['names'] = df_3['names'].apply(lambda x: x.split(".")[0]).astype(int)

  #df_3['names']=df['names'].astype(int)
  df_3 = df_3.groupby('cluster')


  df['cluster'] = df['cluster'].astype(str)  #cluster cahangeing string

 
  #plottinG 2D
  plot_div = plot(px.scatter(df, x="pca_0", y="pca_1",size_max=20,
                 size="max_tfidf_value",hover_data=["name",'cluster',"max_tfidf_value","word_of_max_tfidf"], color="cluster",  template="simple_white",width=900, height=600),
               output_type='div')

  #plottin 3D
  plot_div_3d = plot( px.scatter_3d(df, x="pca_0", y="pca_1",z="pca_2",
              color='cluster',hover_data=["name",'cluster',"max_tfidf_value","word_of_max_tfidf"],template="simple_white", width=950, height=650),
               output_type='div')


  

  context={'plot_div': plot_div,
   "plot_div_3d":plot_div_3d,
   "Cluster_0":  df_2["Cluster :0"].head(),
   "Cluster_1":  df_2["Cluster :1"].head(),
   "Cluster_2":  df_2["Cluster :2"].head(),
  
  
   "Cluster_0_fileName":   df_3.get_group('0'),#df_3.get_group('0').head(10),
   "Cluster_1_fileName":   df_3.get_group('1'),#df_3.get_group("1").head(10),
   "Cluster_2_fileName":   df_3.get_group('2'),#df_3.get_group("2").head(10),


   
   "Cluster_0_links":   df_3.get_group('0')["names"].values.tolist(),#df_3.get_group('0').head(10),
   "Cluster_1_links":   df_3.get_group('1')["names"].values.tolist(),#df_3.get_group("1").head(10),
   "Cluster_2_links":   df_3.get_group('2')["names"].values.tolist(),#df_3.get_group("2").head(10),



   "Number_of_cluster_member":[ len(df_3.get_group('0')),
                                len(df_3.get_group('1')),
                                len(df_3.get_group('2')),
                              ],
    "name":"According to CountVect.",
    "data":df.iloc[:, 1:4].values.tolist()

   }

  return render(request, "index.html",context )
    


    
    
