#include "semaforo-app.hpp"
#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE("SemaforoApp");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED(SemaforoApp);

TypeId
SemaforoApp::GetTypeId()
{
  static TypeId tid = TypeId("SemaforoApp")
    .SetParent<ndn::App>()
    .AddConstructor<SemaforoApp>();
  return tid;
}

void
SemaforoApp::StartApplication()
{
  ndn::App::StartApplication(); // Sempre chamar isso primeiro

  semaforoThread = std::thread(&SemaforoApp::RodarSemaforo, this);
}

void
SemaforoApp::StopApplication()
{
  running = false;
  if (semaforoThread.joinable())
    semaforoThread.join();

  ndn::App::StopApplication();
}

void
SemaforoApp::OnInterest(std::shared_ptr<const ndn::Interest> interest)
{
  NS_LOG_INFO("Semaforo recebeu Interest: " << interest->getName());
  // Aqui você poderia responder com Data ou acionar mudar_estado()
}

void
SemaforoApp::RodarSemaforo()
{
  using namespace std::chrono;
  using namespace std;

  while (running) {
    for (auto& estado : estados) {
        estadoAtual = &estado; // armazena o endereço
        tempo = estado.tempo;

        for (; tempo > 0; --tempo) {
            cout << "Sinal: " << estadoAtual->nome << " (" << tempo << "s)" << endl;
            this_thread::sleep_for(seconds(1));
        }
    }
  }
}

void 
mudar_estado() {
        if (estado_atual == "VERMELHO") {
            this_thread::sleep_for(seconds(3)); // Simula tempo para sinalizar ao outro semáforo
        }
        acabou_de_ceder=true;
        lock_guard<mutex> lock(mtx); // Trava o tempo para alteração segura
        tempo = 0;
    }

bool 
avaliar(float densidade_concorrente) {
    if (estadoAtual == "VERMELHO" && !acabou_de_ceder && densidade_concorrente >= densidade) {
      mudar_estado();
      acabou_de_ceder = true;
      return true;
    }
    return false;
    }    

} // namespace ns3


