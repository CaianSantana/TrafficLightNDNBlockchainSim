#ifndef SEMAFORO_APP_HPP
#define SEMAFORO_APP_HPP

#include "ns3/ndnSIM/apps/ndn-app.hpp"
#include <array>
#include <string>
#include <thread>
#include <chrono>
#include <iostream>

namespace ns3 {

class SemaforoApp : public ndn::App {
public:
  static TypeId GetTypeId();

  virtual void StartApplication() override;
  virtual void StopApplication() override;

  virtual void OnInterest(std::shared_ptr<const ndn::Interest> interest) override;

private:
  std::thread semaforoThread;
  bool running = true;
  bool acabou_de_ceder = false;
  struct Estado {
    std::string nome;
    int tempo;
  };
  Estado* estadoAtual;

  std::array<std::pair<std::string, int>, 3> estados {{
      {"VERDE", 24},
      {"AMARELO", 3},
      {"VERMELHO", 24}
  }};

  void RodarSemaforo();
  void mudar_estado();
  bool avaliar
};

} // namespace ns3

#endif // SEMAFORO_APP_HPP
